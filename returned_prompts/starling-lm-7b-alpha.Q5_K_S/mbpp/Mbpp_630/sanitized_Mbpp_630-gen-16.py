def get_coordinates(test_tup):
  return [
    [test_tup[0]-1, test_tup[1]-1],
    [test_tup[0]-1, test_tup[1]],
    [test_tup[0]-1, test_tup[1]+1],
    [test_tup[0], test_tup[1]-1],
    [test_tup[0], test_tup[1]],
    [test_tup[0], test_tup[1]+1],
    [test_tup[0]+1, test_tup[1]-1],
    [test_tup[0]+1, test_tup[1]],
    [test_tup[0]+1, test_tup[1]+1]
  ]