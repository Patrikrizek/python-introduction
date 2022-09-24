# Conditionals
def check_speed(speed):
  if speed > 70:
    print("over speed limit")
  elif speed == 70:
    print("right speed")
  else:
    print("under speed limit")

check_speed(100)

def check_temperature(c):
  if (c > 30):
    print ('too hot')
    print('aagh')
  elif (c < 0):
    print('too cold')
  else:
    print('perfect')    

check_temperature(28)