
def min_product_tuple(tuples: list) -> int:
  min_product = min(min_product_tuple_pair(tup) for tup in tuples)
  return min_product

def min_product_tuple_pair(tup):
  return min(tup[0]*tup[1], tup[0]*(-tup[1]), (-tup[0])*tup[1])


