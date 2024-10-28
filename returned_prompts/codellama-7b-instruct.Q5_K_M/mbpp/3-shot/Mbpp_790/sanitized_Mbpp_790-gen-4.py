def even_position(my_list):
  return all(my_list[i] % 2 == 0 for i in range(0, len(my_list), 2))