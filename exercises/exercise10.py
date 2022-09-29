name = str(input("Please enter your name: "))
salary = int(input("Please enter your salary: "))

if salary >= 1500:
    tax = salary * 21 / 100
else:
    tax = salary * 10 / 100

net = salary - tax
print("Name: ", name)    
print("Tax: ", tax)    
print("Net: ", net)    