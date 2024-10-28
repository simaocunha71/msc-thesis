def odd_Equivalent(bin_str,rot):
  rotated_str = (bin_str[-rot:] + bin_str[:-rot])
  return sum(1 for i in range(len(bin_str)) if int(rotated_str[i:i+2],2) % 2 != 0)