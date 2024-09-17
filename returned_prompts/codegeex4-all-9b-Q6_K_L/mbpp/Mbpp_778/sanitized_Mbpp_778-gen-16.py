def pack_consecutive_duplicates(lst: list) -> list:
  res = []
  temp = [lst[0]]
  for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
      temp.append(lst[i])
    else:
      res.append(temp)
      temp = [lst[i]]
  res.append(temp)
  return res