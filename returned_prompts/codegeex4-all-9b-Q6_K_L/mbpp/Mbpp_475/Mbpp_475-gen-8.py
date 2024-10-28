def sort_counter(dictionary: dict) -> list:
  sorted_dict = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
  return sorted_dict

