def max_product_tuple(my_list: list) -> int:
  return max(abs(b*c) for a,b in my_list for c in my_list if a==c)