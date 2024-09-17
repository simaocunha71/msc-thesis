
def check_type(input_tuple):
  first_type = type(input_tuple[0])
  return all(isinstance(i, first_type) for i in input_tuple)


