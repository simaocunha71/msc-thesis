def get_ludic(n):
  ludic_nums = []
  ludic_nums.append(1)
  i = 1
  while i <= n:
    if i % 2 == 0:
      ludic_nums.append(i)
    else:
      ludic_nums.append(i + 1)
      i += 2
    i += 1
  return ludic_nums