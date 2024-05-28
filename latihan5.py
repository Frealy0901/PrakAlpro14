def kombinasi(x, y):
    if y == 0 or y == x:
        return 1
    elif y > x:
        return 0
    else:
        return kombinasi(x-1, y-1) + kombinasi(x-1, y)
print(kombinasi(5, 2))  