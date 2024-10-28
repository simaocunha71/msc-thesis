def get_ludic(n):
  ludic_nums = [1]
  i = 2
  while i <= n:
    if i % 2 == 0 or i % 3 == 0:
      i += 1
      continue
    is_ludic = True
    for j in ludic_nums:
      if i % j == 0:
        is_ludic = False
        break
    if is_ludic:
      ludic_nums.append(i)
    i += 1
  return ludic_nums