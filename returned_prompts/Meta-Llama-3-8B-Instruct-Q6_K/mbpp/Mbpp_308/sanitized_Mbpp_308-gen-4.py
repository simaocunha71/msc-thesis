def large_product(list1, list2, n):
  products = [i * j for i in list1 for j in list2]
  return sorted(products, reverse=True)[:n]