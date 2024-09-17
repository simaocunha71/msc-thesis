def odd_Equivalent(str_n: str,n: int) -> int:
  str_n = str_n + str_n + str_n
  count = 0
  for i in range(len(str_n)):
    if int(str_n[i]) % 2 != 0:
      count += 1
  return count