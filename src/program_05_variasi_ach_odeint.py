# Program 5: Pengaruh laju ventilasi (ACH) terhadap CO2 (ODEINT, args)
import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# fungsi model: dC/dt = G + lam*(C_out - C), lam = ACH/60 (1/menit)
def model(C, t, ach):
    V = 168.0
    n, g = 31, 5.0e-6                 # jumlah orang, emisi CO2 (m^3/s/orang)
    C_out = 420.0
    G = n * g * 1e6 * 60 / V          # generasi (ppm/menit)
    lam = ach / 60.0                  # laju pertukaran udara (1/menit)
    return G + lam * (C_out - C)

C0 = 420.0
t = np.linspace(0, 120, 241)

hasil = {}
for ach in [0.5, 1.0, 2.0, 4.0]:
    hasil[ach] = odeint(model, C0, t, args=(ach,))

os.makedirs('../figures', exist_ok=True)
gaya = {0.5: 'r-', 1.0: 'b--', 2.0: 'g:', 4.0: 'm-.'}
for ach, y in hasil.items():
    plt.plot(t, y, gaya[ach], label='ACH = %.1f /jam' % ach)
plt.axhline(1000, color='gray', ls=':', lw=1)
plt.xlabel(r'$t$, (menit)')
plt.ylabel(r'Konsentrasi CO$_2$ $C(t)$, (ppm)')
plt.legend(frameon=False)
plt.grid(alpha=0.3)
plt.savefig('../figures/gambar_03_variasi_ach.png', dpi=150)
plt.show()
for ach, y in hasil.items():
    print('ACH %.1f -> C(120 menit) = %.0f ppm' % (ach, y[-1][0]))
