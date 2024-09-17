
def find_combinations(num_pairs: tuple) -> tuple:
  combinations = []
  for i in range(len(num_pairs)):
    for j in range(i+1, len(num_pairs)):
      combinations.append((num_pairs[i][0] + num_pairs[j][0], num_pairs[i][1] + num_pairs[j][1]))
      combinations.append((num_pairs[j][0] + num_pairs[i][0], num_pairs[j][1] + num_pairs[i][1]))
  return tuple(set(combinations))


