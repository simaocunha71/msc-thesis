def number_ctr(string):
  num_ctr = 0
  for i in string:
    if i.isdigit():
      num_ctr += 1
  return num_ctr