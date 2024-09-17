```
def max_product_tuple(tuples):
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = abs(tuples[i][0] * tuples[i][1] * tuples[j][0] * tuples[j][1])
            if product > max_product:
                max_product = product
    return max_product
```


The function iterates over each pair of tuples in the given list, calculates the absolute product of the numbers in each pair, and keeps track of the maximum product found. The unit test `assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36` suggests that the maximum product is 36, which is the product of (2, 7) and (4, 9). Therefore, the function returns the maximum product found. 





The unit test `assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36` is used to check if the function is working correctly. This test checks if the function returns the maximum product of 36, which is the product of (2, 7) and (4, 9). If the function returns the correct result, the test passes. If the function returns an incorrect result, the test fails. The unit test helps to ensure that the function is working correctly and can be used to catch any bugs or errors in the function.