def swap_List(my_list):
  first_element = my_list[0]
  last_element = my_list[-1]
  my_list[0] = last_element
  my_list[-1] = first_element
  return my_list