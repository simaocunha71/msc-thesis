
def count_integer(my_list):
  return len(list(filter(lambda x: isinstance(x, int), my_list)))


