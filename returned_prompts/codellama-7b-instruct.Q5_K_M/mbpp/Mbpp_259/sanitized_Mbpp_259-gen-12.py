def maximize_elements(tuple1, tuple2):
  result = []
  for i in range(len(tuple1)):
    for j in range(len(tuple2)):
      if tuple1[i][0] == tuple2[j][0]:
        result.append((tuple1[i][0], max(tuple1[i][1], tuple2[j][1])))
  return tuple(result)