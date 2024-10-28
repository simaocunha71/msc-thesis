
def count_Occurrence(my_list: list,my_tuple: tuple) -> dict:
  result = {}
  for element in my_tuple:
    result[element] = my_list.count(element)
  return result


