# Menentukan True / False (Boolean)
sudah_bayar = True
stok_habis = False

if (sudah_bayar):
    print("berhasil")
else:
    print("gagal")

# jadi terjadi berhasil jika data 'true'


# Menyimpan teks (string)
nama = "farras"
umur = '1'

print(nama)
print(umur)

# Menampilkan angka bilangan bulat (integer)
umur = 1
kelas = 1
no_telp =39489834
a = 10
b = 2

print(umur)
print(kelas)
print(no_telp)
print(a + b)


# Menampilkan angka bilangan desimal/koma (float)
harga = 15000.50
tinggi_badan = 170.50
pi = 3.14

print(harga)
print(tinggi_badan)
print(pi)
print(type(harga))

# Operasi matematika
harga = 15000.5
diskon = 0.1    # 10%

potongan = harga * diskon
harga_akhir = harga - potongan

print(f"potongan: {potongan}")
print(f"harga akhir: {harga_akhir}")

# Pembulatan Float 
angka = 3.14159265

print(round(angka))         # dibulatkan ke integer: 3
print(round(angka, 2))      # dibulatkan 2 angka di belakang koma: 3.14


# Menyatakan bilangan dalam format heksa (bilangan berbasis 16) >> (warna) (hexadecimal)
warna = 0x1a2b3c

print(warna)
print(type(warna))

# Convert angka biasa ke hexadecimal
angka = 225
hasil_hex = hex(angka)

print(hasil_hex)        # 0Xfff
print(type(hasil_hex))  # <class 'str'>


# Menyatakan pasangan angka real dan imajiner >> perhitungan matematika (complex)
angka = 1 + 5j

print(angka)
print(type(angka))

# Ambil bagian real dan imajiner
angka + 3 + 4j

print(angka.real)      # 3.0
print(angka.imag)      # 4.0

# Operasi matematika dengan complex
a = 1 + 2j
b = 3 + 4j

print(a + b)       # (4+6j)
print(a * b)       # (-5+10j)


# Menyimmpan banyak data sekaligus dalam satu variabel (urutan terjaga dan bisa diubah (tambah/hapus/edit item)) (List)
buah = ["apel", "jeruk", "mangga"]

print(buah)
print(type(buah))

# Akses item dengan Index (Setiap item di list punya "nomor urut" yang disebut index, dan di Python index dimulai dari 0.)\
print(buah[0])
print(buah[1])
print(buah[2])

# Mengubah Item
buah[0] = "melon"
print(buah)

# Menambah & Menghapus Item
buah.append("pisang")  # append: nambah item di akhir
print(buah)

buah.remove("jeruk")
print(buah)

# Cek jumlah item dalam list
print(len(buah))


# Menyimmpan banyak data sekaligus, bedanya tuple tidak bisa diubah (setelah dibuat disebut immutable) (tuple)
# Perhatikan: tuple >> ( )  list >> [ ].
koordinat = (-6.5971, 106.8060)

print(koordinat)
print(type(koordinat))

# Akses item dengan Index
print(koordinat[0])
print(koordinat[1])


# Kumpulan data unik yang tidak berurutan dan tidak bisa memiliki duplikat dan urutannya terjaga (set)
buah =  {"apel", "jeruk", "apel", "mangga"} # apel 2x

print(buah)
print(type(buah))
# Set gak punya index

# Cek keanggotaan (paling sering dipakai)
buah = {"apel", "jeruk", "mangga"}

print("apel" in buah)       # True
print("durian" in buah)     # False

# Menambah & Menghapus item
buah.add("durian")      # Tambah item
print(buah)

buah.remove("jeruk")    # Hapus item
print(buah)


# Menyimpan data berpasangan key-value (kunci dan nilai) (dictionary)
data_siswa = {"nama": "Haniyya", "id":2, "kelas": "XII IPA"}

print(data_siswa)
print(type(data_siswa))

# Akses data pakai Key
print(data_siswa["nama"])
print(data_siswa["id"])

# Menambah & Mengubah data
data_siswa["umur"] = 17            # Tambah key baru
data_siswa["kelas"] = "XII IPS"    # Ubah value dari key yang sudah ada

# Menghapus data
del data_siswa["umur"]
print(data_siswa)

# Lihat semua key atau semua value
print(data_siswa.keys())     # Semua key: nama, id, kelas
print(data_siswa.values())   # Semua value: Haniyya, 2, XII IPS
