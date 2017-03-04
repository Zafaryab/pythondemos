print("-" * 70)
i = 1
while i <= 10:
    if i != 1:
        print("%02d |      " % i, end=' ')
    else:
        print(" Table: ", end=' ')
    n = 1
    while n <= 10:
        print( "%3d  " % (i * n), end=' ')
        n += 1
    print()
    if i == 1:
         print("-" * 70)
    i += 1
print("-" * 70)
