
def search(s_list:list) -> int:
  if len(s_list) == 0:
    return None
  if len(s_list) == 1:
    return s_list[0]
  else:
    if s_list[0] == s_list[1]:
      return search(s_list[1:])
    elif s_list[-1] == s_list[-2]:
      return search(s_list[:-2])
    else:
      return s_list[0]


