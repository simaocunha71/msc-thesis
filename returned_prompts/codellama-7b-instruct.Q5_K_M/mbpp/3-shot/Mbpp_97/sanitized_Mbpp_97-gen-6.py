def frequency_lists(my_lists: list) -> dict:
  flat_list = [item for sublist in my_lists for item in sublist]
  return {x: flat_list.count(x) for x in set(flat_list)}