# 1. Definisikan fungsi untuk mencetak angka ganjil
def print_odd_numbers(n):
    odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]  # Buat daftar angka ganjil
    return odd_numbers  # Kembalikan daftar angka ganjil

# 2. Minta input dari pengguna untuk nilai n
n = int(input("Masukkan nilai n: "))

# 3. Panggil fungsi print_odd_numbers dengan nilai n yang dimasukkan
odd_numbers_result = print_odd_numbers(n)

# 4. Cetak hasil angka ganjil
print(f"Angka ganjil hingga {n}: {odd_numbers_result}")

# 5. Tambahkan perintah untuk mencetak jumlah total angka ganjil
print(f"Jumlah total angka ganjil hingga {n}: {len(odd_numbers_result)}")
