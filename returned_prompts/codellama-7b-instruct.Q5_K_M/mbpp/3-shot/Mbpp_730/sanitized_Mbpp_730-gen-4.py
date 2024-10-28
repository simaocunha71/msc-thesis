def consecutive_duplicates(my_list):
  new_list = []
  for i in range(len(my_list)):
    if i == 0 or my_list[i] != my_list[i - 1]:
      new_list.append(my_list[i])
  return new_list