def frequency_lists(list_of_lists: list) -> dict:
  flat_list = [item for sublist in list_of_lists for item in sublist]
  return {i: flat_list.count(i) for i in flat_list}