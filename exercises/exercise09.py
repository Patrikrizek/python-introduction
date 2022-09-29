physics = int(input("Please enter your Physics marks: "))
chemistry = int(input("Please enter your Chemistry marks: "))
maths = int(input("Please enter your Maths marks: "))

total = physics + chemistry + maths
percentage = total / 450 * 100

if percentage >= 60:
    print("pass")
else:
    print("fail")