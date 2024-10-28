
def pancake_sort(my_list):
  for i in range(len(my_list)):
    max_index = my_list.index(max(my_list))
    my_list.pop(max_index)
    my_list.insert(0, max(my_list))
  return my_list


