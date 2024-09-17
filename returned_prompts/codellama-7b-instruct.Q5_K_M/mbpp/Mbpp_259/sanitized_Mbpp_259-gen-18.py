def maximize_elements(tup1, tup2):
  tup_list = [tup1, tup2]
  max_tup = max(tup_list, key=lambda x: x[1][1])
  return max_tup