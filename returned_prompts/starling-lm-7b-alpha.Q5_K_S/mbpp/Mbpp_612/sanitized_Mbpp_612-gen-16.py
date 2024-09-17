def merge(tup_of_list):
  first_list = []
  second_list = []
  for i in tup_of_list:
    first_list.append(i[0])
    second_list.append(i[1])
  return [first_list, second_list]