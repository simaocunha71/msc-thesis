
def large_product(list1, list2, n):
  product_list = []
  for i in range(n):
    product_list.append(list1[i] * list2[i])
  return sorted(product_list, reverse=True)[:n]


