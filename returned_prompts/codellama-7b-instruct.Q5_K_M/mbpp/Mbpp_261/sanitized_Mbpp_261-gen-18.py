def division_elements(tuple1, tuple2):
  result = []
  for i in range(len(tuple1)):
    result.append(tuple1[i] / tuple2[i])
  return tuple(result)