# 1. Definisikan fungsi untuk mengevaluasi kinerja
def evaluate_performance(percentage):
    if percentage >= 90:
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Poor performance"

# 2. Minta input dari pengguna untuk persentase siswa
student_percentage = float(input("Masukkan persentase siswa: "))

# 3. Panggil fungsi evaluate_performance dengan persentase siswa yang dimasukkan
result = evaluate_performance(student_percentage)

# 4. Cetak hasil evaluasi kinerja siswa
print(result)

# 5. Tambahkan perintah untuk mengevaluasi beberapa siswa
while True:
    student_percentage = input("Masukkan persentase siswa (atau ketik 'exit' untuk keluar): ")
    if student_percentage.lower() == 'exit':
        break
    result = evaluate_performance(float(student_percentage))
    print(result)
