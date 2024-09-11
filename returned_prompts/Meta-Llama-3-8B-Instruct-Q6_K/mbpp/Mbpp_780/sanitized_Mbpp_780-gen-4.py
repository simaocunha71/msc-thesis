def find_combinations(tuples):
  result = set()
  for i in range(len(tuples)):
    for j in range(i + 1, len(tuples)):
      result.add((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
      result.add((tuples[i][0] + tuples[j][1], tuples[i][1] + tuples[j][0]))
  return list(result)  # convert set to list and return