
def number_ctr(string_input):
  num_ctr = 0
  for char in string_input:
    if char.isdigit():
      num_ctr += 1
  return num_ctr


