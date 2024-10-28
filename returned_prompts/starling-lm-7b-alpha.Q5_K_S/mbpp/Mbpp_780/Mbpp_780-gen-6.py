
def find_combinations(test_tup_list):
  result = []
  for i in range(len(test_tup_list)):
    for j in range(i+1, len(test_tup_list)):
      result.append((test_tup_list[i][0]+test_tup_list[j][0], test_tup_list[i][1]+test_tup_list[j][1]))
  return result


