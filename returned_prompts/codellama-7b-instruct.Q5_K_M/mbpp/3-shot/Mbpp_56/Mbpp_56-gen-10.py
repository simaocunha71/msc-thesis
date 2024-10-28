
def check(num):
  str_num = str(num)
  rev_num = int(str_num[::-1])
  if num == rev_num * 2 - 1:
    return True
  else:
    return False


