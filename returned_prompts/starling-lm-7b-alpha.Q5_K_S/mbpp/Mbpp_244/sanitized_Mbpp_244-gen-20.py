def next_Perfect_Square(num):
  if num < 0:
    return -1
  if num == 0:
    return 0
  if num == 1:
    return 1
  if num % 2 == 0:
    return num + 1
  else:
    i = num + 1
    while i % 2 != 0:
      i += 1
    return i