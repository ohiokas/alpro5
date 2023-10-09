def hitung_frekuensi(kalimat, kata):
    kata_split = kalimat.split()
    frekuensi = kata_split.count(kata)
    return frekuensi

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata = "makan"

frekuensi = hitung_frekuensi(kalimat, kata)
print(f"Kata '{kata}' ada {frekuensi} buah")