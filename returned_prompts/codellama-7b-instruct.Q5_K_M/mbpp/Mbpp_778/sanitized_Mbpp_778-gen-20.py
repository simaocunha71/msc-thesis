def pack_consecutive_duplicates(my_list: list) -> list:
  packed_list = []
  current_list = []
  for i in my_list:
    if current_list and current_list[-1] == i:
      current_list.append(i)
    else:
      if current_list:
        packed_list.append(current_list)
      current_list = [i]
  if current_list:
    packed_list.append(current_list)
  return packed_list