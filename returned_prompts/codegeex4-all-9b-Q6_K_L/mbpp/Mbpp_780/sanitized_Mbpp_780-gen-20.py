def find_combinations(tup_list: list) -> list:
  res = []
  for i in range(len(tup_list)):
    for j in range(i+1, len(tup_list)):
      res.append((tup_list[i][0]+tup_list[j][0], tup_list[i][1]+tup_list[j][1]))
  return res