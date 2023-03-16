# For this task create a program that prints the mirror image of an n-dimensional identity matrix (where n is input by the user).
# An identity matrix is defined as a square matrix with 1's running from the top left of the square to the bottom right. The rest are 0's. The identity matrix has applications ranging from machine learning to the general theory of relativity.

size = 4
print()
print("Inverse Identity matrix") 
for row in range(0, size):
    for col in range(0, size):
      if (col + row == size-1):
          print("1 ", end=" ")
      else:
          print("0 ", end=" ")
    print()
