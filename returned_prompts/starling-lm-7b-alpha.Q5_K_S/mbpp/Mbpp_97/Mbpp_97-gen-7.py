
def frequency_lists(lists: list) -> dict:
  flat_list = [element for sublist in lists for element in sublist]
  frequency_dict = {element: flat_list.count(element) for element in flat_list}
  return frequency_dict


