# Funtions
def marks_average():
    english = int(input("Please enter your English marks: "))
    maths = int(input("Please enter your Maths marks: "))
    science = int(input("Please enter your Science marks: "))

    total = english + maths + science
    average = total / 3
    print("Your average score is:", average)