def pack_consecutive_duplicates(lst):
  result = []
  sub_list = [lst[0]]
  for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
      sub_list.append(lst[i])
    else:
      result.append(sub_list)
      sub_list = [lst[i]]
  result.append(sub_list)
  return result