
def find_combinations(nums_list: list) -> list:
  combinations = []
  for i in range(len(nums_list)):
    for j in range(i+1, len(nums_list)):
      combinations.append((nums_list[i][0] + nums_list[j][0], nums_list[i][1] + nums_list[j][1]))
  return combinations


