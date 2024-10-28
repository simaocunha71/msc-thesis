def find_tuples(test_tup_list, k):
  return [tup for tup in test_tup_list if all(num % k == 0 for num in tup)]