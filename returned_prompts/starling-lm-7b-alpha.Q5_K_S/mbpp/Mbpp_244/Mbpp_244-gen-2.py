
def next_Perfect_Square(n):
  i = n
  while True:
    if i % 2 == 0:
      i += 1
    else:
      i += 2
    if i ** 0.5 == int(i ** 0.5):
      return i


