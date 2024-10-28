def average_tuple(my_tuple):
  my_list = list(my_tuple)
  my_list = [sum(element) / len(element) for element in my_list]
  return my_list