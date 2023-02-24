# For this task you have the chance to show what you’ve learned about implementing repetition in code. You are required to create a program that uses the while loop structure.
# Write a program that always asks the user to enter a number. When the user enters the negative number -1, the program should stop requesting the user to enter a number. The program must then calculate the average of the numbers entered excluding the -1.
# Make use of the while loop repetition structure to implement the program.

num = int(input("Enter whole positive number:"))

if num != -1 and num != 0:
  numbers = num
  
  sum = 0
  while num > 0:
    sum += num
    num -= 1

  print("The average of the numbers is:", round(sum / numbers))

# The next version could also include an average from a negative number.