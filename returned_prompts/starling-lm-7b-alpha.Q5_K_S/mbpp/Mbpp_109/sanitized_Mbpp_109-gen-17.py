def odd_Equivalent(s:str,n:int)->int:
  while len(s) != n:
    s = s[1:]+s[0]
  odd_counter = 0
  for i in range(n):
    if int(s[i]) % 2 != 0:
      odd_counter += 1
  return odd_counter