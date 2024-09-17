def max_length(lst):
  max_len = max(len(sub) for sub in lst)
  max_list = [sub for sub in lst if len(sub) == max_len]
  return (max_len, max_list[0] if max_list else [])