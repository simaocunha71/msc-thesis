
def multiple_to_single(my_list):
  str_list = str(my_list)
  single_int = int(str_list.replace('[', '').replace(']', ''))
  return single_int


