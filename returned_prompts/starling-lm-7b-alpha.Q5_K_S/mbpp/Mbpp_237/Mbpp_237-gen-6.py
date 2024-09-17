
def check_occurences(list_of_tuples: list) -> dict:
  occurences = {}
  for tuple in list_of_tuples:
    if tuple not in occurences:
      occurences[tuple] = 1
    else:
      occurences[tuple] += 1
  return occurences


