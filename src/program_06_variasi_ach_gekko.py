# Program 6: Pengaruh laju ventilasi (ACH) terhadap CO2 (GEKKO)
import os
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

V, C_out = 168.0, 420.0
G = 31 * 5.0e-6 * 1e6 * 60 / V           # generasi CO2 (ppm/menit)

m = GEKKO(remote=False)
m.time = np.linspace(0, 120, 241)
ach = m.Param()                          # laju ventilasi (parameter yang diubah-ubah)
C = m.Var(420.0)
m.Equation(C.dt() == G + (ach / 60.0) * (C_out - C))

m.options.IMODE = 4
m.options.TIME_SHIFT = 0

os.makedirs('../figures', exist_ok=True)
for nilai, gaya in zip([0.5, 1.0, 2.0, 4.0], ['r-', 'b--', 'g:', 'm-.']):
    ach.value = nilai
    m.solve(disp=False)
    plt.plot(m.time, C.value, gaya, linewidth=2, label='ACH = %.1f /jam' % nilai)

plt.axhline(1000, color='gray', ls=':', lw=1)
plt.xlabel(r'$t$, (menit)')
plt.ylabel(r'Konsentrasi CO$_2$ $C(t)$, (ppm)')
plt.legend(frameon=False); plt.grid(alpha=0.3)
plt.savefig('../figures/gambar_03b_variasi_ach_gekko.png', dpi=150)
plt.show()
