def find_combinations(tup_list):
  result = set()
  for i in range(len(tup_list)):
    for j in range(i+1, len(tup_list)):
      result.add(tup_list[i][0] + tup_list[j][0])
      result.add(tup_list[i][1] + tup_list[j][1])
  return sorted(list(result))