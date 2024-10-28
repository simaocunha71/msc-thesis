def large_product(l1,l2,k):
  products = sorted([i*j for i in l1 for j in l2], reverse=True)
  return products[:k]