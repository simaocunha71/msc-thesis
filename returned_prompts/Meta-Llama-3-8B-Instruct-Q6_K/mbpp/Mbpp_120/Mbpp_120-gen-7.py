```
def max_product_tuple(tuples):
    max_product = float('-inf')
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = abs(tuples[i][0]*tuples[j][0] - tuples[i][1]*tuples[j][1])
            if product > max_product:
                max_product = product
    return max_product
```


The problem is asking to find the maximum absolute product between numbers in pairs of tuples within a given list. For example, given the list [(2, 7), (2, 6), (1, 8), (4, 9)], the maximum absolute product is the product of the numbers in the tuples (2, 7) and (1, 8), which is |2*1 - 7*8| = 36.

The function max_product_tuple takes a list of tuples as input and returns the maximum absolute product. It iterates over each pair of tuples in the list, calculates the absolute product of the numbers in the tuples, and keeps track of the maximum product found.

The unit test `assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36` helps to clarify the problem and ensures that the function is working correctly. It checks that the function returns 36 when given the list [(2, 7), (2, 6), (1, 8), (4, 9)]. If the function is working correctly, it will pass this test. If not, it will fail and provide an error message that helps to identify the problem.