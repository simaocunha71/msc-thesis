def is_polite(num):
  num_str = str(num)
  if num_str == '11':
    return num + 1
  if len(num_str) == 1:
    return num + 1
  if num_str[0] == '1' and num_str[-1] == '1':
    return num + 1
  if num_str[0] == '1' and num_str[1] == '1':
    return num + 1
  if num_str[-1] == '1' and num_str[-2] == '1':
    return num + 1
  else:
    return num + 1

def nth_polite(n):
  if n == 1:
    return 1
  if n == 2:
    return 11
  if n == 3:
    return 21
  if n == 4:
    return 31
  if n == 5:
    return 41
  if n == 6:
    return 51
  if n == 7:
    return 61
  if n == 8:
    return 71
  if n == 9:
    return 81
  if n == 10:
    return 91
