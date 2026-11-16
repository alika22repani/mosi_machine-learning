# Program 8: Respon CO2 terhadap input step okupansi (GEKKO)
import os
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO(remote=False)
m.time = np.linspace(0, 120, 1201)

ustep = np.zeros(1201)
ustep[200:] = 1660.7                 # step pada t = 20 menit (indeks 200)
u = m.Param(value=ustep)

C = m.Var(800.0)
m.Equation(30 * C.dt() == -(C - 420.0) + u)

m.options.IMODE = 4
m.solve(disp=False)

os.makedirs('../figures', exist_ok=True)
plt.plot(m.time, C.value, 'r-', label=r'Output $C(t)$')
plt.plot(m.time, ustep + 420, 'b-', label=r'Input $C_{out}+\Delta C_{ss}\,s(t)$')
plt.xlabel(r'$t$, (menit)'); plt.ylabel('ppm')
plt.legend(loc='best'); plt.grid(alpha=0.3)
plt.savefig('../figures/gambar_04b_step_gekko.png', dpi=150)
plt.show()
