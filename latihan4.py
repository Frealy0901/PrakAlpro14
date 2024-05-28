def jumlah_digit(n):
    if n < 10:
        return n
    else:
        return n % 10 + jumlah_digit(n // 10)

try:
    bilangan = int(input("Masukkan bilangan: "))
    if bilangan >= 0:
        result = jumlah_digit(bilangan)
        print(f"Jumlah digit dari {bilangan} adalah {result}.")
    else:
        print("Masukkan harus lebih besar atau sama dengan 0.")
except ValueError:
    print("Masukkan harus berupa bilangan bulat.")