def remove_kth_element(my_list,k):
  new_list = my_list[:k] + my_list[k+1:]
  return new_list