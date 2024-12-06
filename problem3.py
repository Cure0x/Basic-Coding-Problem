def calculate_Grade(siswa):
    final_Grade = ((30/100)*siswa[1]) +  ((35/100)*siswa[2]) + ((35/100)*siswa[3])
    return final_Grade

def define_Grade (nilai):
    if nilai > 85 and nilai <= 100:
        huruf, angka, ket = 'A', 4 , 'Lulus'
    elif nilai > 80 and nilai <= 85:
        huruf, angka, ket = 'A-', 3.7 , 'Lulus'
    elif nilai > 75 and nilai <= 80:
        huruf, angka, ket = 'B+', 3.3 , 'Lulus'
    elif nilai > 70 and nilai <= 75:
        huruf, angka, ket = 'B', 3.0 , 'Lulus'
    elif nilai > 65 and nilai <= 70:
        huruf, angka, ket = 'B-', 2.7 , 'Lulus'
    elif nilai > 60 and nilai <= 65:
        huruf, angka, ket = 'C+', 2.3 , 'Lulus'
    elif nilai > 55 and nilai <= 60:
        huruf, angka, ket = 'C', 2.0 , 'Lulus'
    elif nilai > 50 and nilai <= 55:
        huruf, angka, ket = 'C-', 1.7 , 'Belum Lulus'
    elif nilai > 45 and nilai <= 50:
        huruf, angka, ket = 'D', 1 , 'Belum Lulus'
    elif nilai > 0 and nilai <= 45:
        huruf, angka, ket = 'E', 0 , 'Belum Lulus'
    else:
        huruf, angka, ket = 'ERROR', 0, 'CEK DATA KEMBALI'
    return [huruf, angka, ket]

da_Sis = [
    ['Adi', 80,80,86],
    ['Budi', 65,80,70],
    ['Cepi', 60,60,70],
    ['Dedi', 50,70,50],
    ['Abu', 90,80,70],
    ['Baskara', 65,80,75],
    ['Elang', 55,60,55]
]

print("Grading Siswa")
print(f"\n No.       Nama Mahasiswa      Nilai Akhir     Huruf      Angka       Keterangan")

for i, siswa in enumerate (da_Sis):
    final_Grade = calculate_Grade(siswa)
    nilai = define_Grade(final_Grade)
    print(f"  {i+1}             {siswa[0]}                {final_Grade}             {nilai[0]}         {nilai[1]}          {nilai[2]}")