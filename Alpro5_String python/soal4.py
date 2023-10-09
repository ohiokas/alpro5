def cari_kata_terpendek_terpanjang(kalimat):
    # Memisahkan kata-kata dalam kalimat menjadi sebuah list
    kata_kalimat = kalimat.split()

    # Menginisialisasi kata terpendek dan terpanjang dengan kata pertama dalam kalimat
    kata_terpendek = kata_kalimat[0]
    kata_terpanjang = kata_kalimat[0]

    # Mencari kata terpendek dan terpanjang dalam kalimat
    for kata in kata_kalimat:
        if len(kata) < len(kata_terpendek):
            kata_terpendek = kata
        if len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata

    return kata_terpendek, kata_terpanjang

# Contoh penggunaan program
kalimat = "red snakes and a black frog in the pool"

# Memanggil fungsi cari_kata_terpendek_terpanjang untuk mencari kata terpendek dan terpanjang
kata_terpendek, kata_terpanjang = cari_kata_terpendek_terpanjang(kalimat)

# Menampilkan output
print(f"terpendek: {kata_terpendek}, terpanjang: {kata_terpanjang}")