def is_Diff(num):
  num_str = str(num)
  if len(num_str) % 2 == 0:
    even_sum = sum(int(num_str[i]) for i in range(0, len(num_str), 2))
    odd_sum = sum(int(num_str[i]) for i in range(1, len(num_str), 2))
  else:
    even_sum = sum(int(num_str[i]) for i in range(1, len(num_str), 2))
    odd_sum = sum(int(num_str[i]) for i in range(0, len(num_str), 2))
  return (even_sum - odd_sum) % 11 == 0