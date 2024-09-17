
def large_product(list_a,list_b,n):
  largest_products = []
  for i in range(n):
    largest_products.append(list_a[i]*list_b[i])
  largest_products.sort(reverse=True)
  return largest_products


