def sort_counter(dic: dict):
  return sorted(dic.items(), key=lambda x: x[1], reverse=True)