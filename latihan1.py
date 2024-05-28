def is_prime(n, divisor=2):
    if n <= 1:
        return False
    elif divisor * divisor > n:
        return True
    elif n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor + 1)

try:
    bilangan = int(input("Masukkan bilangan: "))
    if is_prime(bilangan):
        print(f"{bilangan} adalah bilangan prima.")
    else:
        print(f"{bilangan} bukan bilangan prima.")
except ValueError:
    print("Masukkan harus berupa bilangan bulat.")