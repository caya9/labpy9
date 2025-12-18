# Teks awal
txt = "Hello World"

# 1. Hitung jumlah karakter
jumlah_karakter = len(txt)
print("Jumlah karakter:", jumlah_karakter)

# 2. Ambil karakter terakhir
karakter_terakhir = txt[-1]
print("Karakter terakhir:", karakter_terakhir)

# 3. Ambil karakter index ke-2 sampai index ke-4 (llo)
substring = txt[2:5]
print("Index ke-2 sampai ke-4:", substring)

# 4. Hilangkan spasi pada text (HelloWorld)
tanpa_spasi = txt.replace(" ", "")
print("Tanpa spasi:", tanpa_spasi)

# 5. Ubah text menjadi huruf besar
huruf_besar = txt.upper()
print("Huruf besar:", huruf_besar)

# 6. Ubah text menjadi huruf kecil
huruf_kecil = txt.lower()
print("Huruf kecil:", huruf_kecil)

# 7. Ganti karakter H dengan karakter J
ganti_karakter = txt.replace("H", "J")
print("Ganti H dengan J:", ganti_karakter)
