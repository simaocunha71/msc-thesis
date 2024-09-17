def get_ludic(n):
  ludic = []
  for i in range(1, n+1):
    if i % 2 == 0:
      continue
    elif i % 5 == 0:
      continue
    ludic.append(i)
  return ludic