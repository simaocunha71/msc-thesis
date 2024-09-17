def max_length(lists: list) -> tuple:
  max_len = 0
  max_list = None
  for li in lists:
    if len(li) > max_len:
      max_len = len(li)
      max_list = li
  return (max_len, max_list)