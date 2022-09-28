def larger_num(a, b, c):
  if a > b:
    if a > c:
      print(a)
    else:
      print(c)
  elif b > c:
    print(b)
  else:
    print(c)
larger_num(228, 67, 93)