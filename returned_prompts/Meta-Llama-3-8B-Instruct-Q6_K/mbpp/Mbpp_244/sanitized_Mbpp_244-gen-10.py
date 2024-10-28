def next_Perfect_Square(n):
  i = n
  while True:
    i += 1
    root = int(i**0.5)
    if root * root == i:
      return i
    if i > n:
      return i