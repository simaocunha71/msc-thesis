def large_product(list1: list,list2: list,n: int) -> list:
  products = []
  for i in range(len(list1)):
    products.append(list1[i]*list2[i])
  return sorted(products, reverse=True)[:n]