def max_product_tuple(tuples: list):
  max_product = 0
  for i in range(len(tuples)):
    for j in range(i+1, len(tuples)):
      max_product = max(max_product, abs(tuples[i][0] * tuples[j][0]), abs(tuples[i][1] * tuples[j][1]))
  return max_product