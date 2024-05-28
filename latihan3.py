def jumlah_deret_ganjil(n):
    if n == 1:
        return 1
    else:
        return jumlah_deret_ganjil(n-1) + (n*2 - 1)
print(jumlah_deret_ganjil(5))  # Output: 25