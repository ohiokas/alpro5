def is_anagram(str1, str2):
    # Menghitung jumlah huruf pada kedua kata
    count1 = {}
    count2 = {}

    # Menghitung jumlah huruf pada kata pertama
    for letter in str1:
        if letter in count1:
            count1[letter] += 1
        else:
            count1[letter] = 1

    # Menghitung jumlah huruf pada kata kedua
    for letter in str2:
        if letter in count2:
            count2[letter] += 1
        else:
            count2[letter] = 1

    # Mengbandingkan jumlah huruf pada kedua kata
    if len(count1) != len(count2):
        return False

    for letter in count1:
        if letter not in count2 or count1[letter] != count2[letter]:
            return False

    return True

# Mengambil input dari pengguna
str1 = input("Masukkan kata pertama: ")
str2 = input("Masukkan kata kedua: ")

# Menghitung apakah kedua kata adalah anagram atau bukan
result = is_anagram(str1, str2)

# Menampilkan hasil
if result:
    print("Kata tersebut adalah anagram.")
else:
    print("Kata tersebut bukan anagram.")