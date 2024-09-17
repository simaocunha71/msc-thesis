def next_power_of_2(n):
  if n<1:
    return 1
  else:
    return 2**(int(math.log(n,2))+1)