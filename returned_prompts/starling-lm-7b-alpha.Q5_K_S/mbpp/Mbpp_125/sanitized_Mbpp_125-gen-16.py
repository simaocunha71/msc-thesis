def find_length(bin_string:str)->int:
  max_diff = 0
  for i in range(len(bin_string)):
    max_diff = max(max_diff, bin_string.count("0", 0, i+1) + bin_string.count("1", i+1, len(bin_string)))
  return max_diff