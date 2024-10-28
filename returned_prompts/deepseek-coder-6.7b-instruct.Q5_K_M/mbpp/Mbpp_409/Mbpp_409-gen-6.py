
def min_product_tuple(tuples_list: list) -> int:
  return min(x[0]*x[1] for x in tuples_list)


