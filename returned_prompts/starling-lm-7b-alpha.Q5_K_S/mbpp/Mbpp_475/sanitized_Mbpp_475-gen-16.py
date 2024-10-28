def sort_counter(dict1:dict):
  return sorted(dict1.items(), key=lambda kv: kv[1], reverse=True)