n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

for i in range(n, m+1):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)