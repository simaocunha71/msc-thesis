def frequency_lists(lists: list) -> dict:
  flattened_list = [num for sublist in lists for num in sublist]
  return {num: flattened_list.count(num) for num in flattened_list}

