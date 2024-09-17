def large_product(list1: list, list2: list, n: int) -> list:
  large_products = []
  for num1 in list1:
    for num2 in list2:
      large_products.append(num1 * num2)
  return sorted(large_products, reverse=True)[:n]