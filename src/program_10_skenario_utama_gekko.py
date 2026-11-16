# Program 10: Skenario utama (GEKKO) - strategi u divariasikan dengan FV
import os
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

V, C_out, g = 168.0, 420.0, 5.0e-6
ACH0, ACH_MAX = 0.5, 6.0

m = GEKKO(remote=False)
t = np.linspace(0, 240, 481)
m.time = t

n_arr = np.where((t < 90) | ((t >= 105) & (t < 195)), 31.0, 0.0)
n = m.Param(value=n_arr)             # jumlah orang di kelas (berubah terhadap waktu)
u = m.FV(0.0)                        # strategi ventilasi (0-1)

C = m.Var(C_out)
G = n * g * 1e6 * 60 / V
lam = (ACH0 + ACH_MAX * u) / 60.0
m.Equation(C.dt() == G + lam * (C_out - C))

m.options.IMODE = 4
m.options.TIME_SHIFT = 0
m.options.NODES = 3

os.makedirs('../figures', exist_ok=True)
plt.figure(figsize=(9, 5))
for uu, w in zip([0.0, 0.1, 0.3, 1.0], ['r', 'orange', 'g', 'b']):
    u.value = uu
    m.solve(disp=False)
    plt.plot(m.time, C.value, color=w, label='u = %.1f' % uu)
plt.axhline(1000, color='gray', ls=':')
plt.xlabel('Waktu (menit)'); plt.ylabel('CO2 (ppm)')
plt.legend(frameon=False); plt.grid(alpha=0.3)
plt.savefig('../figures/gambar_05b_skenario_gekko.png', dpi=150)
plt.show()
