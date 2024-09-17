def is_undulating(num):
  num_str = str(num)
  for i in range(len(num_str)-2):
    if num_str[i] == num_str[i+1] or num_str[i+1] != num_str[i+2]:
      return False
  return True