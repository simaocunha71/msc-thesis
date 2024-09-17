def sort_counter(d:dict) -> list:
  sorted_d = sorted(d.items(), key = lambda kv:(kv[1], kv[0]))
  return sorted_d