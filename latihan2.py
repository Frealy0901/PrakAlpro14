def is_palindrome(s):
    # Basis: Jika panjang kalimat kurang dari atau sama dengan 1, maka palindrom
    if len(s) <= 1:
        return True
    # Jika karakter pertama dan terakhir tidak sama, bukan palindrom
    elif s[0] != s[-1]:
        return False
    # Rekursi: Cek sisa kalimat tanpa karakter pertama dan terakhir
    else:
        return is_palindrome(s[1:-1])

# Contoh penggunaan
kalimat = input("Masukkan kalimat: ").lower()  # Ubah ke huruf kecil untuk memperhitungkan kapitalisasi
if is_palindrome(kalimat):
    print(f"'{kalimat}' adalah palindrom.")
else:
    print(f"'{kalimat}' bukan palindrom.")
