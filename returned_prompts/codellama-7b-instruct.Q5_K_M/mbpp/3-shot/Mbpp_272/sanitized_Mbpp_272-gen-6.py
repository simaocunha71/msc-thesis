def rear_extract(list_of_tuples: list) -> list:
  rear_list = []
  for tup in list_of_tuples:
    rear_list.append(tup[2])
  return rear_list