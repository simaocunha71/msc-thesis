
def Find_Max(str_list: list) -> list:
  max_len = 0
  max_element = ''
  for i in str_list:
    if len(i) > max_len:
      max_element = i
      max_len = len(i)
  return max_element


