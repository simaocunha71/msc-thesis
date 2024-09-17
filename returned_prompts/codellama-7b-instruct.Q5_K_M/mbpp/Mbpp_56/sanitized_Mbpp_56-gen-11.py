def check(num):
  str_num = str(num)
  rev = int(str_num[::-1])
  if (num-1)==rev*2:
    return True
  else:
    return False