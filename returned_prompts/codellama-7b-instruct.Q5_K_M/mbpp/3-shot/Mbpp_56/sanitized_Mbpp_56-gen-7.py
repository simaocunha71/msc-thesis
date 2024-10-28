def check(num):
  if (str(num)[::-1] == str(num)[:-1]):
    return True
  else:
    return False