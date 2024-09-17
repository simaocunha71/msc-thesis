def merge(lists: list) -> list:
  first_list = []
  second_list = []
  for i in lists:
    first_list.append(i[0])
    second_list.append(i[1])
  return [first_list, second_list]