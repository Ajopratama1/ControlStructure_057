# 1. Definisikan fungsi untuk menemukan angka terbesar
def find_largest(a, b, c):
    return max(a, b, c)

# 2. Minta input dari pengguna untuk angka pertama
num1 = float(input("Masukkan angka pertama: "))

# 3. Minta input dari pengguna untuk angka kedua
num2 = float(input("Masukkan angka kedua: "))

# 4. Minta input dari pengguna untuk angka ketiga
num3 = float(input("Masukkan angka ketiga: "))

# 5. Temukan dan cetak angka terbesar
largest = find_largest(num1, num2, num3)
print(f"Angka terbesar adalah: {largest}")
