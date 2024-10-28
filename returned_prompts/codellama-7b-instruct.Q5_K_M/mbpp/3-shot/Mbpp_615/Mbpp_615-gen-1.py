
def average_tuple(tup: tuple) -> list:
  avg_list = []
  for sub_tuple in tup:
    avg = sum(sub_tuple) / len(sub_tuple)
    avg_list.append(avg)
  return avg_list


