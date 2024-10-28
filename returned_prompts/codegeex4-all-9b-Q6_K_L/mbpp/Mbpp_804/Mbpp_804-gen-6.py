def is_product_even(lst: list) -> bool:
  product = 1
  for num in lst:
    product *= num
  return product % 2 == 0