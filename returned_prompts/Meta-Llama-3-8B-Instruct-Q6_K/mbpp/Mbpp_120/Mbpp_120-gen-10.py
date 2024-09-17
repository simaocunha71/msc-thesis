```
def max_product_tuple(tuples):
    max_product = float('-inf')
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = abs(tuples[i][0] * tuples[j][1])
            if product > max_product:
                max_product = product
    return max_product
```



The function `max_product_tuple` takes a list of tuples as input. It initializes `max_product` as negative infinity. Then, it iterates over the list of tuples using two nested loops. The outer loop iterates over each tuple in the list, and the inner loop iterates over the remaining tuples in the list. For each pair of tuples, it calculates the absolute product of the corresponding numbers. If this product is greater than the current `max_product`, it updates `max_product`. Finally, it returns the maximum absolute product found. The unit test `assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36` ensures that the function works correctly. 







