# Program 3: CO2 di ruang kelas, ventilasi DIKENDALIKAN oleh jendela (ODEINT)
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ---- model: V dC/dt = c_g*u_g - (Q0 + c_v*u_v)*(C - C_out) ----
def kelas(C, t, cg, cv, ug, uv):
    V = 168.0                       # volume ruang kelas (m^3)
    Q0 = 1.4                        # infiltrasi dasar = 0.5 ACH (m^3/menit)
    C_out = 420.0                   # CO2 udara luar (ppm)
    Q = Q0 + cv * uv                # laju ventilasi total (m^3/menit)
    dCdt = (cg * ug - Q * (C - C_out)) / V
    return dCdt

ts = np.linspace(0, 120, 121)       # 0-120 menit, setiap 1 menit

cg = 93.0                           # koefisien generasi (ppm.m^3/menit per %)
cv = 0.168                          # koefisien ventilasi (m^3/menit per % bukaan)

ug = np.zeros(121)                  # ug = okupansi (%)
ug[20:80] = 100.0                   # kelas terisi menit 20-80
uv = np.zeros(121)                  # uv = bukaan jendela (%)
uv[40:60] = 50.0                    # jendela dibuka 50% menit 40-60
uv[60:90] = 100.0                   # jendela dibuka 100% menit 60-90

C0 = 420.0
z = np.zeros(121)
z[0] = C0

# input ditahan konstan (zero-order hold) selama interval [t_i, t_i+1]
for i in range(120):
    y = odeint(kelas, C0, [0, 1], args=(cg, cv, ug[i], uv[i]))
    C0 = y[-1][0]
    z[i + 1] = C0

os.makedirs('../figures', exist_ok=True)
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(ts, z, 'b-')
plt.axhline(1000, color='gray', ls=':', label='Batas 1000 ppm')
plt.ylabel(r'Konsentrasi CO$_2$ $C(t)$, (ppm)')
plt.legend(frameon=False)
plt.grid(alpha=0.3)
plt.subplot(2, 1, 2)
plt.plot(ts, ug, 'r--', label=r'$u_g$ (okupansi)')
plt.plot(ts, uv, 'g--', label=r'$u_v$ (bukaan jendela)')
plt.ylabel(r'Input $u(t)$, (%)')
plt.xlabel(r'$t$, (menit)')
plt.legend(frameon=False)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/gambar_02_dikendalikan.png', dpi=150)
plt.show()
print('C maksimum = %.1f ppm pada t = %.0f menit' % (z.max(), ts[z.argmax()]))
