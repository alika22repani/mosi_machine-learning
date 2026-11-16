# Program 1: CO2 di ruang kelas, ventilasi TERTUTUP (ODEINT)
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ---- model ruang kelas: dC/dt = c*u / V  ----
def kelas(C, t, c, u):
    V = 168.0                 # volume ruang kelas (m^3) = 8 x 7 x 3
    dCdt = (c / V) * u        # laju kenaikan CO2 (ppm/menit)
    return dCdt

# waktu simulasi 0-120 menit, setiap 1 menit
ts = np.linspace(0, 120, 121)

# koefisien generasi CO2 (ppm.m^3/menit per % okupansi)
# c = n * g * 1e6 * 60 / 100 = 31 * 5e-6 * 1e6 * 60 / 100 = 93
c = 93.0
u = np.zeros(121)             # u = okupansi kelas (%)
u[20:80] = 100.0              # kelas terisi penuh antara menit 20 s.d. 80

C0 = 420.0                    # kondisi awal = CO2 udara luar (ppm)
z = np.zeros(121)
z[0] = C0

# simulasi dengan ODEINT, langkah demi langkah (cara yang sama seperti contoh)
for i in range(120):
    okupansi = u[i]           # u ditahan konstan selama interval [t_i, t_i+1]
    y = odeint(kelas, C0, [0, 1], args=(c, okupansi))
    C0 = y[-1][0]             # ambil titik terakhir
    z[i + 1] = C0

# plot hasil
os.makedirs('../figures', exist_ok=True)
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(ts, z, 'b-')
plt.ylabel(r'Konsentrasi CO$_2$ $C(t)$, (ppm)')
plt.grid(alpha=0.3)
plt.subplot(2, 1, 2)
plt.plot(ts, u, 'r--')
plt.ylabel(r'Okupansi $u(t)$, (%)')
plt.xlabel(r'$t$, (menit)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/gambar_01_tertutup.png', dpi=150)
plt.show()
print('C maksimum = %.1f ppm' % z.max())
