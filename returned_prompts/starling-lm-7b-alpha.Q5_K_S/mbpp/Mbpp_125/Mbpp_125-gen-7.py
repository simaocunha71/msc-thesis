
def find_length(binary_string):
  max_diff = 0
  for i in range(len(binary_string)):
    max_diff = max(max_diff, binary_string.count('1') - binary_string[:i+1].count('1'))
  return max_diff


