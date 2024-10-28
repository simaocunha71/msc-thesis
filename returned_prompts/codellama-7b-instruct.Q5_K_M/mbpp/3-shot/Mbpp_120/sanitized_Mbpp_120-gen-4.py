def max_product_tuple(num_tuples):
  max_product = 0
  for i in range(len(num_tuples)):
    for j in range(i, len(num_tuples)):
      product = abs(num_tuples[i][0] * num_tuples[i][1] * num_tuples[j][0] * num_tuples[j][1])
      if product > max_product:
        max_product = product
  return max_product