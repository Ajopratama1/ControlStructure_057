# 1. Definisikan fungsi untuk mencetak desain
def print_design(n):
    for i in range(1, n + 1):  # Iterasi dari 1 hingga n
        print((str(i) + ' ') * i)  # Cetak angka i sebanyak i kali, diikuti spasi

# 2. Minta input dari pengguna untuk nilai n
n = int(input("Masukkan nilai n: "))

# 3. Panggil fungsi print_design dengan nilai n yang dimasukkan
print_design(n)

# 4. Tambahkan perintah untuk mencetak garis pemisah setelah desain
print("-" * 20)

# 5. Tambahkan perintah untuk mencetak jumlah total baris yang dicetak
print(f"Jumlah total baris yang dicetak: {n}")
