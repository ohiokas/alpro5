def hapus_spasi(kalimat):
    # Memisahkan kata-kata dalam kalimat menjadi sebuah list
    kata_kalimat = kalimat.split()

    # Menggabungkan kembali kata-kata menjadi string dengan satu spasi normal
    kalimat_baru = " ".join(kata_kalimat)

    return kalimat_baru

# Contoh penggunaan program
kalimat = "saya tidak suka      memancing ikan      "

# Memanggil fungsi hapus_spasi untuk menghapus spasi berlebih
hasil = hapus_spasi(kalimat)

# Menampilkan output
print(hasil)