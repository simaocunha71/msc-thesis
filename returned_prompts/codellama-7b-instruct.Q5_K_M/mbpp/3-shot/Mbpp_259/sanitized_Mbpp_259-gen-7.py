def maximize_elements(tuple1, tuple2):
  new_tuple1 = []
  new_tuple2 = []
  for i in range(len(tuple1)):
    if tuple1[i][0] > tuple2[i][0]:
      new_tuple1.append(tuple1[i])
      new_tuple2.append(tuple2[i])
    else:
      new_tuple1.append(tuple2[i])
      new_tuple2.append(tuple1[i])
  return tuple(new_tuple1), tuple(new_tuple2)