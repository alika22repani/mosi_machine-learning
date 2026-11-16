# Program 11: Verifikasi perhitungan manual (metode Euler) vs solusi analitik vs ODEINT
import numpy as np
from scipy.integrate import odeint

# Kasus: kelas terisi 31 orang, ACH = 2 /jam, C(0) = 420 ppm
V, n, g, C_out, ach = 168.0, 31, 5.0e-6, 420.0, 2.0
G = n * g * 1e6 * 60 / V            # generasi (ppm/menit)      -> 55.357
lam = ach / 60.0                    # laju ventilasi (1/menit)  -> 0.03333
tau = 1 / lam                       # konstanta waktu (menit)   -> 30
Css = C_out + G / lam               # keadaan tunak (ppm)       -> 2080.7
print('G = %.3f ppm/menit, lambda = %.5f /menit, tau = %.1f menit, Css = %.1f ppm' % (G, lam, tau, Css))

dt = 5.0                            # langkah Euler (menit)
t = np.arange(0, 60 + dt, dt)
C_euler = np.zeros_like(t); C_euler[0] = 420.0
for k in range(len(t) - 1):
    dCdt = G + lam * (C_out - C_euler[k])
    C_euler[k + 1] = C_euler[k] + dt * dCdt

C_an = Css - (Css - 420.0) * np.exp(-t / tau)              # solusi analitik
C_ode = odeint(lambda C, tt: G + lam * (C_out - C), 420.0, t)[:, 0]

print('%5s %10s %10s %10s %10s %10s' % ('t', 'Euler', 'Analitik', 'ODEINT', 'Err Euler', 'Err %'))
for k in range(len(t)):
    e = C_euler[k] - C_an[k]
    print('%5.0f %10.1f %10.1f %10.1f %10.1f %10.2f' % (t[k], C_euler[k], C_an[k], C_ode[k], e, 100 * e / C_an[k]))

# waktu mencapai 1000 ppm (analitik)
t1000 = -tau * np.log((Css - 1000) / (Css - 420))
print('Waktu mencapai 1000 ppm = %.1f menit' % t1000)
