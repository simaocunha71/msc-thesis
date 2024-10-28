def sort_counter(dictionary:dict) -> list:
  return sorted(dictionary.items(), key = lambda kv:(kv[1], kv[0]))