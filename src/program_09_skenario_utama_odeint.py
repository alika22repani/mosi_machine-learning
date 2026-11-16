# Program 9: Skenario utama - strategi ventilasi u pada kelas selama 240 menit (ODEINT)
import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

V = 168.0                 # volume kelas (m^3)
C_out = 420.0             # CO2 udara luar (ppm)
g = 5.0e-6                # emisi CO2 per orang (m^3/s)
ACH0 = 0.5                # infiltrasi dasar (1/jam)
ACH_MAX = 6.0             # tambahan ACH saat jendela/pintu terbuka penuh (u = 1)

def jumlah_orang(t):
    # kelas 1: 0-90 menit | istirahat: 90-105 | kelas 2: 105-195 | kosong: > 195
    if t < 90 or (105 <= t < 195):
        return 31
    return 0

# model: dC/dt = n*g*1e6*60/V + lam*(C_out - C), lam = (ACH0 + ACH_MAX*u)/60
def kelas(C, t, u):
    n = jumlah_orang(t)
    G = n * g * 1e6 * 60 / V
    lam = (ACH0 + ACH_MAX * u) / 60.0
    return G + lam * (C_out - C)

t = np.linspace(0, 240, 2401)
skenario = {0.0: 'Tertutup (u=0)', 0.1: 'Bukaan kecil (u=0.1)',
            0.3: 'Bukaan sedang (u=0.3)', 1.0: 'Terbuka penuh (u=1)'}
warna = {0.0: 'r', 0.1: 'orange', 0.3: 'g', 1.0: 'b'}

os.makedirs('../figures', exist_ok=True)
plt.figure(figsize=(9, 5))
print('%-24s %8s %12s %12s %14s' % ('Skenario', 'C maks', '>1000 ppm', '>1500 ppm', 'C rata2 kelas'))
ada = np.array([jumlah_orang(x) > 0 for x in t])   # penanda saat kelas terisi
for u, nama in skenario.items():
    C = odeint(kelas, C_out, t, args=(u,), tcrit=[90, 105, 195], hmax=0.5)[:, 0]
    plt.plot(t, C, color=warna[u], label=nama)
    print('%-24s %8.0f %10.0f m %10.0f m %12.0f' % (nama, C.max(), (C > 1000).sum() * 0.1,
          (C > 1500).sum() * 0.1, C[ada].mean()))
plt.axhline(1000, color='gray', ls=':')
plt.axvspan(90, 105, color='gray', alpha=0.15)
plt.axvspan(195, 240, color='gray', alpha=0.15)
plt.xlabel('Waktu (menit)')
plt.ylabel(r'Konsentrasi CO$_2$ (ppm)')
plt.legend(frameon=False)
plt.grid(alpha=0.3)
plt.savefig('../figures/gambar_05_skenario_utama.png', dpi=150)
plt.show()
