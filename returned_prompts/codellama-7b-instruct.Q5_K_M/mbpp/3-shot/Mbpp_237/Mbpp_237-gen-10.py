
def check_occurences(my_list_of_tuples: list) -> dict:
  my_dict = {}
  for i in my_list_of_tuples:
    if i in my_dict:
      my_dict[i] += 1
    else:
      my_dict[i] = 1
  return my_dict


