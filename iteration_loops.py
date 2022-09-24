# Iteration
def test_while_loop():
  count = 0
  while count < 10:
    print('h')
    count = count + 1

test_while_loop()

print('\n \n')

def test_for_loop():
  for i in range(11):
    print(i)
    
test_for_loop()

print('\n \n')

def test_for_break_loop():
  for i in range(101):
    print(i)
    if i == 20:
      break

test_for_break_loop()

print('\n \n')

def test_for_continue_loop():
  for i in range(15):
    if i == 5:
      continue
    print(i)

test_for_continue_loop()