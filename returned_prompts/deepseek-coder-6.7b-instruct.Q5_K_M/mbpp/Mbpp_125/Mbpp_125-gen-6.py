
def find_length(bin_str):
  count_0 = bin_str.count('0')
  count_1 = bin_str.count('1')
  return abs(count_0 - count_1)


