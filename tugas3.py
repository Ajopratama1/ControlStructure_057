# 1. Definisikan fungsi untuk menghasilkan deret Fibonacci
def fibonacci_series(n):
    fib_sequence = []  # Inisialisasi daftar untuk menyimpan deret Fibonacci
    a, b = 0, 1  # Inisialisasi dua angka pertama dalam deret Fibonacci
    while a <= n:  # Selama angka a kurang dari atau sama dengan n
        fib_sequence.append(a)  # Tambahkan angka a ke dalam daftar
        a, b = b, a + b  # Update nilai a dan b untuk langkah berikutnya
    return fib_sequence  # Kembalikan deret Fibonacci yang telah dihasilkan

# 2. Minta input dari pengguna untuk nilai n
n = int(input("Masukkan nilai n: "))

# 3. Panggil fungsi fibonacci_series dengan nilai n yang dimasukkan
fibonacci_result = fibonacci_series(n)

# 4. Cetak hasil deret Fibonacci
print(f"Deret Fibonacci hingga {n}: {fibonacci_result}")

# 5. Tambahkan perintah untuk mencetak jumlah total angka dalam deret Fibonacci
print(f"Jumlah total angka dalam deret Fibonacci hingga {n}: {len(fibonacci_result)}")
