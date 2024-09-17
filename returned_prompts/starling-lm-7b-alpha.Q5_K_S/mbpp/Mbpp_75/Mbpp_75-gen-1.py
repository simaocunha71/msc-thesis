
def find_tuples(test_tup, k):
  return [tup for tup in test_tup if all(i%k==0 for i in tup)]


