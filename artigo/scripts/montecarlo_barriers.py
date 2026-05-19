"""Monte Carlo propagation of ASTM A877/A877M valve-spring tolerances
through the deterministic indicators of the BowTie diagram.

The forward model is anchored at the nominal indicator values reported
in Section "Quantitative evaluation of the preventive barriers" of the
manuscript:
    Outer spring: tau_a = 199 MPa, tau_m = 456 MPa, n_f = 1.27,
                  M = 0.78 mm, f_n/f_cam = 3.81
    Inner spring: tau_a = 374 MPa, tau_m = 858 MPa, n_f = 0.68,
                  M = 2.38 mm, f_n/f_cam = 6.85

Variability sources (truncated Gaussian, three sigma = tolerance band):
    L0:    +/- 1.5 percent  (ASTM A877/A877M free-length tolerance)
    d:     +/- 0.5 percent  (ASTM A877/A877M wire diameter tolerance)
    Dm:    +/- 1.0 percent  (typical machining)
    Na:    +/- 0.5 active coil (absolute)
    G:     +/- 3.0 percent  (Shigley 2020, table 10-4)
    Sse:   +/- 8.0 percent  (Shigley 2020, section 10-30, shot-peened wire)
    Ssu:   +/- 4.0 percent
    F_seat:+/- 3.0 percent  (preload measurement)
    H_open:+/- 0.5 percent  (cam-train assembly clearance)

Sensitivity coefficients are derived analytically from the Wahl stress
formula (tau ~ F * Dm / d^3), Shigley's spring stiffness
(k ~ G * d^4 / (Dm^3 * Na)), and Shigley's surge frequency
(f_n ~ (d / (Na * Dm^2)) * sqrt(G / rho)), then convolved with the
nominal indicator values.
"""

from __future__ import annotations
import numpy as np

rng = np.random.default_rng(seed=20260519)
N_TRIALS = 200_000

# -- Nominal values from the manuscript (anchored forward model) -----------
# Stresses in Pa
TAU_A_OUT, TAU_M_OUT = 199e6, 456e6
TAU_A_IN,  TAU_M_IN  = 374e6, 858e6
SSE_NOM = 465e6
SSU_NOM = 1270e6

# Geometric / dynamic baseline values
M_OUT_NOM_MM   = 0.78
M_IN_NOM_MM    = 2.38
FN_OUT_NOM_HZ  = 318.0
FN_IN_NOM_HZ   = 571.0
F_CAM_MAX_HZ   = 83.33

# Tolerances (3-sigma = tolerance)
TOL = dict(
    L0=0.015, d=0.005, Dm=0.010,
    Na_abs=0.50,                   # absolute active-coil tolerance
    G=0.030,
    Sse=0.080, Ssu=0.040,
    F_seat=0.030, H_open=0.005,
)

def gnormal(mu, rel_tol, size=N_TRIALS):
    """Gaussian draw with mean mu and 3*sigma = rel_tol*mu."""
    sigma = mu * rel_tol / 3.0
    return rng.normal(mu, sigma, size)

def gnormal_abs(mu, abs_3sigma, size=N_TRIALS):
    return rng.normal(mu, abs_3sigma / 3.0, size)

# --------------------------------------------------------------------------
# Per-spring Monte Carlo
# --------------------------------------------------------------------------
def run_spring(label, tau_a_nom, tau_m_nom, M_nom_mm, fn_nom_hz):
    # --- Stress propagation ---
    # tau scales as F * Dm / d^3, with F ~ stiffness * compression
    # so tau has the multiplicative composition:
    #   d(tau)/tau = d(F)/F + d(Dm)/Dm - 3 d(d)/d
    # and d(F)/F ~ d(k)/k + d(compression)/compression, with
    #   d(k)/k = d(G)/G + 4 d(d)/d - 3 d(Dm)/Dm - d(Na)/Na
    # so substituting and collecting:
    #   d(tau)/tau = d(G)/G + d(d)/d - 2 d(Dm)/Dm - d(Na)/Na
    #                + d(comp)/comp
    # We draw each source independently and combine.
    fG  = gnormal(1.0, TOL['G'])
    fd  = gnormal(1.0, TOL['d'])
    fDm = gnormal(1.0, TOL['Dm'])
    fNa = 1.0 + gnormal_abs(0.0, TOL['Na_abs']) / 6.0  # 6 active coils baseline
    fHo = gnormal(1.0, TOL['H_open'])
    fFs = gnormal(1.0, TOL['F_seat'])
    # composite factor on tau
    f_tau = fG * fd * (fDm)**(-2) * (fNa)**(-1)
    # compression varies with L0 and H_open; we use F_seat tolerance as the
    # aggregate proxy on the seat-stress contribution
    tau_a = tau_a_nom * f_tau * fFs   # alternating stress
    tau_m = tau_m_nom * f_tau * fFs   # mean stress (same correlation)
    # Strength
    Sse = gnormal(SSE_NOM, TOL['Sse'])
    Ssu = gnormal(SSU_NOM, TOL['Ssu'])
    # Goodman FoS
    inv_nf = tau_a / Sse + tau_m / Ssu
    nf = 1.0 / inv_nf

    # --- Coil-bind margin ---
    # M = H_open - H_solid, H_solid = Nt * d, both with tolerance
    # tolerance on H_open and on d / Nt; we propagate at the M-level
    # with combined sigma based on the dominant terms
    # sigma_M^2 = sigma(H_open)^2 + sigma(H_solid)^2
    # H_solid ~ 33.6 mm (outer) or 32.0 mm (inner) at baseline
    H_solid_nom = 33.6 if label == "OUTER" else 32.0
    sigma_Hopen = 34.38 * TOL['H_open'] / 3.0
    sigma_Hsolid = H_solid_nom * np.sqrt(TOL['d']**2 + (TOL['Na_abs']/6.0)**2) / 3.0
    delta_H = rng.normal(0, sigma_Hopen, N_TRIALS) - rng.normal(0, sigma_Hsolid, N_TRIALS)
    M_mm = M_nom_mm + delta_H

    # --- Natural-frequency ratio ---
    # fn ~ (d / (Na * Dm^2)) * sqrt(G / rho); rho deterministic
    # d(fn)/fn = d(d)/d - d(Na)/Na - 2 d(Dm)/Dm + 0.5 d(G)/G
    f_fn = fd * (fNa)**(-1) * (fDm)**(-2) * np.sqrt(fG)
    fn = fn_nom_hz * f_fn
    fn_ratio = fn / F_CAM_MAX_HZ

    # --- Reporting ---
    P_M_fail   = float(np.mean(M_mm < 1.5))
    P_nf_fail  = float(np.mean(nf < 1.0))
    P_fn_fail  = float(np.mean(fn_ratio < 4.0))
    q05_nf, q50_nf, q95_nf = np.quantile(nf, [0.05, 0.50, 0.95])
    q05_M, q50_M, q95_M    = np.quantile(M_mm, [0.05, 0.50, 0.95])
    q05_fr, q50_fr, q95_fr = np.quantile(fn_ratio, [0.05, 0.50, 0.95])

    print(f"--- {label} spring ---")
    print(f"  M (coil-bind) [mm]:  median={q50_M:.3f}  "
          f"[5,95]=[{q05_M:.3f}, {q95_M:.3f}]  "
          f"P[M<1.5]={P_M_fail*100:.2f}%")
    print(f"  n_f (Goodman):       median={q50_nf:.3f}  "
          f"[5,95]=[{q05_nf:.3f}, {q95_nf:.3f}]  "
          f"P[n_f<1]={P_nf_fail*100:.2f}%")
    print(f"  fn/fcam:             median={q50_fr:.3f}  "
          f"[5,95]=[{q05_fr:.3f}, {q95_fr:.3f}]  "
          f"P[fn/fcam<4]={P_fn_fail*100:.2f}%")
    print(f"  fn [Hz]:             median={np.median(fn):.1f}  "
          f"[5,95]=[{np.quantile(fn,0.05):.1f}, {np.quantile(fn,0.95):.1f}]")
    return dict(
        M_q=(q05_M, q50_M, q95_M), P_M=P_M_fail,
        nf_q=(q05_nf, q50_nf, q95_nf), P_nf=P_nf_fail,
        fr_q=(q05_fr, q50_fr, q95_fr), P_fn=P_fn_fail,
    )

if __name__ == "__main__":
    print(f"Monte Carlo: {N_TRIALS:,} trials, RNG seed = 20260519\n")
    out = run_spring("OUTER", TAU_A_OUT, TAU_M_OUT, M_OUT_NOM_MM, FN_OUT_NOM_HZ)
    print()
    inn = run_spring("INNER", TAU_A_IN,  TAU_M_IN,  M_IN_NOM_MM,  FN_IN_NOM_HZ)
