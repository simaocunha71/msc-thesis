def large_product(list1: list, list2: list, n: int) -> list:
  product_list = [a * b for a in list1 for b in list2]
  largest_products = sorted(product_list, reverse=True)[:n]
  return largest_products