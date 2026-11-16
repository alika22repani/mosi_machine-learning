# Pemodelan & Simulasi Dinamika Konsentrasi CO₂ di Ruang Kelas

Tugas Pemodelan Sistem Dinamik – model satu-zona (*well-mixed*) neraca massa CO₂:

    V dC/dt = n·g·10^6 − Q (C − C_out)

## Struktur
| File | Isi |
|---|---|
| `CO2_Kelas_Pemodelan_Sistem_Dinamik.ipynb` | Notebook Google Colab (semua program + hasil) |
| `src/program_01..02` | Kasus 1: ventilasi tertutup (ODEINT, GEKKO) |
| `src/program_03..04` | Kasus 2: ventilasi dikendalikan jendela |
| `src/program_05..06` | Kasus 3: variasi laju ventilasi (ACH) |
| `src/program_07..08` | Kasus 4: respon step okupansi |
| `src/program_09..10` | Kasus 5: skenario utama (strategi ventilasi u) |
| `src/program_11` | Verifikasi perhitungan manual (Euler vs analitik) |
| `figures/` | Hasil grafik simulasi |

## Menjalankan
```bash
pip install -r requirements.txt
cd src
python program_01_tertutup_odeint.py
```
Di Google Colab: buka notebook, jalankan sel pertama (`!pip install gekko`), lalu *Run all*.

## Referensi
Indrazno Siradjuddin, *Pemodelan Sistem Dinamik*.
