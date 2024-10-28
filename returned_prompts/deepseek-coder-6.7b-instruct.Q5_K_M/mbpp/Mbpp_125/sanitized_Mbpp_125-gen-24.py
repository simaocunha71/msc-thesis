def find_length(s):
  count_0 = s.count('0')
  count_1 = s.count('1')
  return abs(count_0 - count_1)