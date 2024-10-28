def odd_Equivalent(bin_string, rotate_times):
  bin_string = bin_string * rotate_times
  odd_count = 0
  for i in range(len(bin_string)):
    if bin_string[i] == "1":
      odd_count += 1
  return odd_count