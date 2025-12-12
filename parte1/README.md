# Parte 1 - TID2025-2

Esta carpeta está reservada para la primera parte del proyecto.
Para la implementación completa, consulta [../parte2/](../parte2/)

from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Params:
    C_m:   float = 9.5e-3
    S_L:   float = 1.9
    S_ir:  float = 2.5e8
    tau_ep:  float = 1e-6
    tau_res: float = 1e-3
    V_th:   float = 1.5
    k_beta: float = 40.0
    I0:      float = 100.0
    t_start: float = 0.0
    pw:      float = 1e-4
    T_per:   float = 1e-3
    N_puls:  int   = 1
    t0:    float = 0.0
    t1:    float = 3e-4
    SOURCE_MODE: str = "current"  # "current" o "voltage"
    V_app_amp: float = 2.0
    seed: int = 0

def beta_sigmoid(lam: np.ndarray, V_th: float, k_beta: float) -> np.ndarray:
    x = np.clip(k_beta * (lam - V_th), -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(-x))

def Iim_pulse_train(t: float, I0: float, t0: float, width: float, period: float, n_pulses: int) -> float:
    if t < t0:
        return 0.0
    m = int((t - t0) // period)
    if (0 <= m < n_pulses) and ((t - t0) - m*period < width):
        return I0
    return 0.0

def V_app_rect(t: float, V_amp: float, t0: float, width: float) -> float:
    return V_amp if (t0 <= t < t0 + width) else 0.0

def simulate_euler_explicit(dt: float, p: Params) -> Dict[str, np.ndarray]:
    N = int(np.ceil((p.t1 - p.t0) / dt))
    t = p.t0 + np.arange(N + 1) * dt
    t[-1] = p.t1

    V = np.zeros_like(t)
    X = np.zeros_like(t)
    X[0] = 0
    S_tilde = np.zeros_like(t)
    Iim = np.zeros_like(t)
    beta_vals = np.zeros_like(t)

    S_tilde[0] = p.S_L + (p.S_ir - p.S_L) * X[0]
    if p.SOURCE_MODE == "current":
        Iim[0] = Iim_pulse_train(t[0], p.I0, p.t_start, p.pw, p.T_per, p.N_puls)
    else:
        Iim[0] = S_tilde[0] * V_app_rect(t[0], p.V_app_amp, p.t_start, p.pw)

    for n in range(N):
        lam = abs(V[n])
        b   = beta_sigmoid(lam, p.V_th, p.k_beta)
        beta_vals[n] = b

        dXdt_ep  = (b - X[n]) / p.tau_ep
        dXdt_res = (b - X[n]) / p.tau_res
        dXdt     = dXdt_ep if dXdt_ep > dXdt_res else dXdt_res
        X[n+1]   = X[n] + dt * dXdt
        if X[n+1] < 0.0: X[n+1] = 0.0
        if X[n+1] > 1.0: X[n+1] = 1.0

        S_tilde[n] = p.S_L + (p.S_ir - p.S_L) * X[n]
        if p.SOURCE_MODE == "current":
            Iim[n] = Iim_pulse_train(t[n], p.I0, p.t_start, p.pw, p.T_per, p.N_puls)
        else:
            Iim[n] = S_tilde[n] * V_app_rect(t[n], p.V_app_amp, p.t_start, p.pw)

        dVdt   = (Iim[n] - S_tilde[n] * V[n]) / p.C_m
        V[n+1] = V[n] + dt * dVdt

    S_tilde[-1] = p.S_L + (p.S_ir - p.S_L) * X[-1]
    beta_vals[-1] = beta_sigmoid(abs(V[-1]), p.V_th, p.k_beta)
    if p.SOURCE_MODE == "current":
        Iim[-1] = Iim_pulse_train(t[-1], p.I0, p.t_start, p.pw, p.T_per, p.N_puls)
    else:
        Iim[-1] = S_tilde[-1] * V_app_rect(t[-1], p.V_app_amp, p.t_start, p.pw)


    return dict(t=t, V=V, X=X, S=S_tilde, I=Iim, beta=beta_vals)

def nice_axes(ax, label, legend=True):
    ax.set_ylabel(label)
    ax.grid(True, alpha=0.3)
    if legend: ax.legend(loc="upper right", frameon=False)

def plot_time_series(results: Dict[str, np.ndarray], dt: float, title_suffix: str = ""):
    t = results["t"]; I = results["I"]; V = results["V"]
    X = results["X"]; S = results["S"]; beta = results["beta"]
    fig, axs = plt.subplots(5, 1, sharex=True, figsize=(9, 9))
    fig.suptitle(f"Electropermeabilización – Euler explícito (dt={dt:g} s)", fontsize=13)
    axs[0].plot(t, I, lw=2, label="I_im(t)"); nice_axes(axs[0], "I_im [A/m²]")
    axs[1].plot(t, V, lw=2, label="V(t)"); nice_axes(axs[1], "V [V]")
    axs[2].plot(t, beta, lw=2, label="β(|V|)"); nice_axes(axs[2], "β")
    axs[3].plot(t, X, lw=2, label="X(t)"); axs[3].set_ylim(-0.05, 1.05); nice_axes(axs[3], "X ∈ [0,1]")
    axs[4].plot(t, S, lw=2, label="S̃(t)"); nice_axes(axs[4], "S̃ [S/m²]"); axs[4].set_xlabel("tiempo [s]")
    plt.tight_layout(rect=[0, 0.02, 1, 0.97]); plt.show()

def compare_dt(dt_list: List[float], p: Params, which: str = "V"):
    assert which in ("V", "X")
    fig, ax = plt.subplots(figsize=(16, 9))
    for dt in dt_list:
        res = simulate_euler_explicit(dt, p)
        y = res[which]
        ax.plot(res["t"], y, label=f"{which}(t)  dt={dt:g}")
        print(f"MODE: {p.SOURCE_MODE}, I0={p.I0:g} A/m^2, pw={p.pw:g}s, dt={dt:g}s")
        print(f"V_max = {np.max(res['V']):.6e} V  at t = {res['t'][np.argmax(res['V'])]:.3e} s")
        print(f"X_max = {np.max(res['X']):.6e}")
        print(f"S_tilde range: [{np.min(res['S']):.6e}, {np.max(res['S']):.6e}] S/m^2")
        
    nice_axes(ax, f"{which}(t)"); ax.set_title(f"Convergencia temporal – {which}(t)"); ax.set_xlabel("tiempo [s]")
    plt.tight_layout(); plt.show()

def main():
    p = Params()
    dt = 1e-9
    res = simulate_euler_explicit(dt, p)
    plot_time_series(res, dt)
    dt_list = [1e-7, 5e-8, 1e-8, 5e-9, 1e-9]
    #compare_dt(dt_list, p, which="V")
    #compare_dt(dt_list, p, which="X")

if __name__ == "__main__":
    main()
