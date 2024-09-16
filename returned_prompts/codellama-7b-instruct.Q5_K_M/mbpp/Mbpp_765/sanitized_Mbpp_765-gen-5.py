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