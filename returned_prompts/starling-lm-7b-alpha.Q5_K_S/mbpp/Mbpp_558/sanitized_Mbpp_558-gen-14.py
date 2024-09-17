def digit_distance_nums(n1,n2):
  n1_str = str(n1)
  n2_str = str(n2)
  if len(n1_str) != len(n2_str):
    raise ValueError('Length of two numbers should be same')
  return sum([abs(int(n1_str[i]) - int(n2_str[i])) for i in range(len(n1_str))])