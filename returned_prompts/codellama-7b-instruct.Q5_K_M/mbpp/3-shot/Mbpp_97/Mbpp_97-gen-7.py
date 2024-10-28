
def frequency_lists(lists: list) -> dict:
  flat_list = [item for sublist in lists for item in sublist]
  return {item: flat_list.count(item) for item in set(flat_list)}


