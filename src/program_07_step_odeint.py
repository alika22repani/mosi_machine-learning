# Program 7: Respon CO2 terhadap input step okupansi (orde satu, ODEINT)
import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# tau * dC/dt = -(C - C_out) + dC_ss * s(t)
def model(C, t):
    tau = 30.0                       # konstanta waktu = V/Q = 1/lambda (menit), ACH = 2
    C_out = 420.0
    dC_ss = 1660.7                   # kenaikan CO2 keadaan tunak: G/lambda (ppm)
    # step okupansi: kelas kosong sampai t = 20, lalu terisi 31 orang
    s = 0.0 if t < 20.0 else 1.0
    return (-(C - C_out) + dC_ss * s) / tau

C0 = 800.0                           # sisa CO2 dari pelajaran sebelumnya (ppm)
t = np.linspace(0, 120, 1201)
C = odeint(model, C0, t, tcrit=[20.0])   # tcrit: titik diskontinu input

os.makedirs('../figures', exist_ok=True)
plt.plot(t, C, 'r-', label=r'Output, $C(t)$')
plt.plot([0, 20, 20, 120], [420, 420, 2080.7, 2080.7], 'b-', label=r'Target tunak $C_{ss}$ (input)')
plt.xlabel(r'$t$, (menit)')
plt.ylabel(r'Konsentrasi CO$_2$, (ppm)')
plt.legend(loc='best', frameon=False)
plt.grid(alpha=0.3)
plt.savefig('../figures/gambar_04_step.png', dpi=150)
plt.show()
print('C(120) = %.1f ppm' % C[-1][0])
