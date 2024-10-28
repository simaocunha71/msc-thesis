def freq_count(my_list: list) -> dict:
  my_dict = {}
  for element in my_list:
    if element not in my_dict:
      my_dict[element] = 1
    else:
      my_dict[element] += 1
  return my_dict