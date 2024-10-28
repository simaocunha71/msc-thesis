def number_ctr(input_string:str)->int:
  count = 0
  for i in input_string:
    if i.isdigit():
      count += 1
  return count