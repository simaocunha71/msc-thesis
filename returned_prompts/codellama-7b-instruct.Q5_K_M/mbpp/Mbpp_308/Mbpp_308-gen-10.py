
def large_product(list1: list,list2: list,n: int) -> list:
  largest_products = []
  for i in range(n):
    largest_products.append(list1[i]*list2[i])
  return sorted(largest_products,reverse=True)


