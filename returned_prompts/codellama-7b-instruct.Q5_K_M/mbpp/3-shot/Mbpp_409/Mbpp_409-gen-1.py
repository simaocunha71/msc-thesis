
def min_product_tuple(num_pairs: list) -> int:
  return min([num_pair[0]*num_pair[1] for num_pair in num_pairs])


