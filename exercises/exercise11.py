n = int(input("Please enter a number: "))

if n >= 1000:
    print("B")
    if n >= 2000:
        print("C")
    else:
        print("D")    
else:
    print("A")    