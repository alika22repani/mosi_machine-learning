# Program 2: CO2 di ruang kelas, ventilasi TERTUTUP (GEKKO)
import os
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

V = 168.0                          # volume ruang kelas (m^3)
c = 93.0                           # koefisien generasi CO2 (ppm.m^3/menit per %)

m = GEKKO(remote=False)            # buat model GEKKO
m.time = np.linspace(0, 120, 121)  # titik waktu (menit)

ustep = np.zeros(121)
ustep[21:81] = 100.0               # okupansi 100% antara menit 20-80
                                   # (GEKKO memakai nilai input di akhir interval -> indeks digeser 1)
u = m.Param(value=ustep)           # input okupansi (%)

C = m.Var(420.0)                   # konsentrasi CO2 awal (ppm)
m.Equation(C.dt() == (c / V) * u)  # persamaan diferensial

m.options.IMODE = 4                # simulasi dinamik
m.solve(disp=False)

os.makedirs('../figures', exist_ok=True)
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(m.time, C.value, 'b-')
plt.ylabel(r'Konsentrasi CO$_2$ $C(t)$, (ppm)')
plt.grid(alpha=0.3)
plt.subplot(2, 1, 2)
plt.plot(m.time, ustep, 'r--')
plt.ylabel(r'Okupansi $u(t)$, (%)')
plt.xlabel(r'$t$, (menit)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/gambar_01b_tertutup_gekko.png', dpi=150)
plt.show()
print('C maksimum = %.1f ppm' % max(C.value))
