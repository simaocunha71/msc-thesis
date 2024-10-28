
def extract_singly(list_of_list):
  flat_list = []
  for sub_list in list_of_list:
    flat_list.extend(sub_list)
  return set(flat_list)


