
def swap_List(my_list: list) -> list:
  first = my_list[0]
  last = my_list[-1]
  my_list[0] = last
  my_list[-1] = first
  return my_list


