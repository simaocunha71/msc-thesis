def next_Perfect_Square(num):
  root = int(num ** 0.5)
  while root ** 2 != num:
    root += 1
  return root ** 2