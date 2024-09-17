```
def min_product_tuple(lst):
    min_product = float('inf')
    for pair in lst:
        product = pair[0] * pair[1]
        if product < min_product:
            min_product = product
    return min_product
```


The function `min_product_tuple` iterates over each pair of tuples in the given list. It calculates the product of each pair and keeps track of the minimum product found so far. The function returns the minimum product found. This is achieved by comparing the product of each pair with the current minimum product, and updating the minimum product if a smaller product is found. The function assumes that the input list contains only pairs of tuples, and returns the minimum product as an integer. If the input list is empty, the function will return positive infinity. 





The unit test `assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8` checks if the function correctly finds the minimum product from the given list of tuples. The expected output is `8`, which is the product of the pair `(1, 8)`. The function correctly identifies this pair as the one with the minimum product and returns `8` as the result.