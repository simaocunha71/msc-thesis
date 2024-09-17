def remove_kth_element(my_list: list, k: int) -> list:
  return my_list[:k] + my_list[k+1:]