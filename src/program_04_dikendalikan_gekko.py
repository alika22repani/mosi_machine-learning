# Program 4: CO2 di ruang kelas, ventilasi DIKENDALIKAN (GEKKO)
import os
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

V, Q0, C_out = 168.0, 1.4, 420.0
cg, cv = 93.0, 0.168

m = GEKKO(remote=False)
m.time = np.linspace(0, 120, 121)

# GEKKO memakai nilai input di akhir interval -> indeks digeser 1
ug_arr = np.zeros(121); ug_arr[21:81] = 100.0
uv_arr = np.zeros(121); uv_arr[41:61] = 50.0; uv_arr[61:91] = 100.0
ug = m.Param(value=ug_arr)
uv = m.Param(value=uv_arr)

C = m.Var(420.0)
m.Equation(V * C.dt() == cg * ug - (Q0 + cv * uv) * (C - C_out))

m.options.IMODE = 4
m.solve(disp=False)

os.makedirs('../figures', exist_ok=True)
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(m.time, C.value, 'b-')
plt.axhline(1000, color='gray', ls=':')
plt.ylabel(r'Konsentrasi CO$_2$ $C(t)$, (ppm)')
plt.grid(alpha=0.3)
plt.subplot(2, 1, 2)
plt.plot(m.time, ug_arr, 'r--', label=r'$u_g$')
plt.plot(m.time, uv_arr, 'g--', label=r'$u_v$')
plt.xlabel(r'$t$, (menit)'); plt.ylabel(r'$u(t)$, (%)')
plt.legend(frameon=False); plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/gambar_02b_dikendalikan_gekko.png', dpi=150)
plt.show()
print('C maksimum = %.1f ppm' % max(C.value))
