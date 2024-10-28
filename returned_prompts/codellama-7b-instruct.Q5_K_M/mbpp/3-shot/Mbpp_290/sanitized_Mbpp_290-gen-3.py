def max_length(my_list: list) -> tuple:
  max_length = 0
  for sub_list in my_list:
    if len(sub_list) > max_length:
      max_length = len(sub_list)
  return (max_length, my_list[max_length])