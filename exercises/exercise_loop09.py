a = 1
while a <= 10:
    if a % 2 == 0:
        b = 1
        while b <= a:
            print(b)
            b = b + 1
        else:
            a = a + 1
    else:
        print(a)
        a = a + 1        