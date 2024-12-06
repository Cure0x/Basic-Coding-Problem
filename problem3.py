def calculate_Grade(siswa):
    final_Grade = ((30/100)*siswa[1]) +  ((35/100)*siswa[2]) + ((35/100)*siswa[3])
    return final_Grade

def define_Grade (nilai, sum_Nilai):
    if nilai > 85 and nilai <= 100:
        huruf, angka, ket = 'A', 4 , 'Lulus'
        sum_Nilai [0] += 1
    elif nilai > 80 and nilai <= 85:
        huruf, angka, ket = 'A-', 3.7 , 'Lulus'
        sum_Nilai [1] += 1
    elif nilai > 75 and nilai <= 80:
        huruf, angka, ket = 'B+', 3.3 , 'Lulus'
        sum_Nilai [2] += 1
    elif nilai > 70 and nilai <= 75:
        huruf, angka, ket = 'B', 3.0 , 'Lulus'
        sum_Nilai [3] += 1
    elif nilai > 65 and nilai <= 70:
        huruf, angka, ket = 'B-', 2.7 , 'Lulus'
        sum_Nilai [4] += 1
    elif nilai > 60 and nilai <= 65:
        huruf, angka, ket = 'C+', 2.3 , 'Lulus'
        sum_Nilai [5] += 1
    elif nilai > 55 and nilai <= 60:
        huruf, angka, ket = 'C', 2.0 , 'Lulus'
        sum_Nilai [6] += 1
    elif nilai > 50 and nilai <= 55:
        huruf, angka, ket = 'C-', 1.7 , 'Belum Lulus'
        sum_Nilai [7] += 1
    elif nilai > 45 and nilai <= 50:
        huruf, angka, ket = 'D', 1 , 'Belum Lulus'
        sum_Nilai [8] += 1
    elif nilai > 0 and nilai <= 45:
        huruf, angka, ket = 'E', 0 , 'Belum Lulus'
        sum_Nilai [9] += 1
    else:
        huruf, angka, ket = 'ERROR', 0, 'CEK DATA KEMBALI'
        sum_Nilai [10] += 1
    return [huruf, angka, ket] , sum_Nilai

da_Sis = [
    ['Adi', 80,80,86],
    ['Budi', 65,80,70],
    ['Cepi', 60,60,70],
    ['Dedi', 50,70,50],
    ['Abu', 90,80,70],
    ['Baskara', 65,80,75],
    ['Elang', 55,60,55]
]

total_Nilai = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Grading Siswa")
print(f"\n No.       Nama Mahasiswa      Nilai Akhir     Huruf      Angka       Keterangan")

for i, siswa in enumerate (da_Sis):
    final_Grade = calculate_Grade(siswa)
    nilai, total_Nilai = define_Grade(final_Grade, total_Nilai)
    print(f"  {i+1}             {siswa[0]}                {final_Grade}             {nilai[0]}         {nilai[1]}          {nilai[2]}")

print(f"\nRekapitulasi Jumlah Nilai: ")

for i,n in enumerate(total_Nilai):
    huruf_Nilai = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E", "ERROR"]
    print(f"Grade {huruf_Nilai[i]} = {n}")
print(f"\nTotal Mahasisiwa = {len(da_Sis)}")