
def merge(list_of_lists: list) -> list:
  first_list = []
  second_list = []
  for i in range(len(list_of_lists)):
    first_list.append(list_of_lists[i][0])
    second_list.append(list_of_lists[i][1])
  return [first_list, second_list]


