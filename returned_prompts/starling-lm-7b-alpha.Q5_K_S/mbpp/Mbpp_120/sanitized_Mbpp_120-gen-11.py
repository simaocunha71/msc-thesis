def max_product_tuple(tup_list: list) -> int:
  max_product = -float("inf")
  for tup in tup_list:
    for i in range(len(tup)-1):
      max_product = max(max_product, tup[i] * tup[i+1] if tup[i+1] > 0 else -(tup[i] * tup[i+1]))
  return max_product