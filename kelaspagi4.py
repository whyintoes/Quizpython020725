# Diberikan data mahasiswa dalam bentuk list of tuple.
# Setiap tuple berisi: (nama, nilai)

mahasiswa = [
    ("Ani", 80),
    ("Budi", 70),
    ("Citra", 85),
    ("Dedi", 65),
    ("Eka", 90)
]

# TUGAS:
# 1. Cetak nama mahasiswa yang memiliki nilai di atas 75.
for nama, nilai in mahasiswa:
    if nilai > 75:
        print(nama)
# 2. Hitung dan cetak rata-rata nilai dari semua mahasiswa.
total_nilai = sum(nilai for _, nilai in mahasiswa)
rata_rata = total_nilai / len(mahasiswa)
print(f"Rata-rata nilai: {rata_rata}")

print("-2-")

# Diberikan daftar produk, masing-masing berupa tuple (nama_produk, harga)

produk = [
    ("Sabun", 10000),
    ("Sampo", 25000),
    ("Pasta Gigi", 15000),
    ("Tisu", 5000)
]

# 1. Buat list baru yang berisi NAMA PRODUK dalam huruf kapital semua.
list_produk = [nama_produk.upper() for nama_produk, _ in produk]
print("Daftar Produk:")
for nama_produk in list_produk:
    print(nama_produk)
# 2. Hitung total harga dari semua produk dan tampilkan.
total_harga = sum(harga for _, harga in produk)
print(f"Total Harga Produk: {total_harga}")