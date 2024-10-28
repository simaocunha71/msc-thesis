def get_ludic(n):
  lucid_nums = []
  for i in range(1, n+1):
    if i % 2 == 0 and i % 3 == 0:
      lucid_nums.append(i)
  return lucid_nums

