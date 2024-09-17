
def recursive_list_sum(list1):
  return sum(list1) if not isinstance(list1[0], list) else recursive_list_sum([x for sublist in list1 for x in sublist])


