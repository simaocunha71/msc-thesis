def find_tuples(tuples, k):
  divisible_tuples = []
  for tuple in tuples:
    if all(i%k == 0 for i in tuple):
      divisible_tuples.append(tuple)
  return divisible_tuples