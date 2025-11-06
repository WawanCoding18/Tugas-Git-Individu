#Nama: Dzakwan Al iman
#NIM: 2504556
#Kelas: 1A

#Studi Kasus-2
import numpy as np

#Nilai siswa
nilai_siswa = np.array([ 85, 90, 78, 88, 92,75, 83, 95, 80, 77,
    89, 94, 70, 76, 84,
    91, 73, 96, 82, 79,
    87, 93, 74, 81, 72,
    69, 97, 68, 86, 99])

nilai_siswa_urut_besar_to_kecil = np.sort(nilai_siswa)[::-1]
Tampilan_nilai_5_terbesar = ", ".join(map(str, nilai_siswa_urut_besar_to_kecil[:5] ))

print("Nilai 5 terbesar:",Tampilan_nilai_5_terbesar)
print("Nilai Rata-rata siswa 5 terbesar: ", np.mean(nilai_siswa_urut_besar_to_kecil[:5]))
