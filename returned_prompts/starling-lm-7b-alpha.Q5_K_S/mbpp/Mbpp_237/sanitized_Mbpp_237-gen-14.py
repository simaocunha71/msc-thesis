def check_occurences(test_list):
  occurences = {}
  for tuple in test_list:
    if tuple in occurences:
      occurences[tuple] += 1
    else:
      occurences[tuple] = 1
  return occurences