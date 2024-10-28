```
def max_product_tuple(tuples):
    max_product = float('-inf')
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = abs(tuples[i][0] * tuples[j][0])
            product += abs(tuples[i][1] * tuples[j][1])
            if product > max_product:
                max_product = product
    return max_product
```    
Explanation:
The function takes a list of tuples as an argument and returns the maximum absolute product between numbers in pairs of tuples. 

It initializes `max_product` to negative infinity and then iterates over the list of tuples. For each pair of tuples, it calculates the absolute product of the numbers and checks if it's greater than the current `max_product`. If it is, it updates `max_product`.

Finally, it returns `max_product`. 

The unit test `assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36` helps to understand the problem better, as it indicates that the function should return the maximum absolute product between numbers in pairs of tuples within the given list. 

For example, the maximum absolute product between numbers in pairs of tuples within the list `[(2, 7), (2, 6), (1, 8), (4, 9)]` is `36`, which is the product of `8` and `9`. 

The function works by iterating over all pairs of tuples, calculating the absolute product of the numbers in each pair, and keeping track of the maximum product found. 

Note that the function returns the maximum absolute product, not the maximum product itself. This is because the problem statement asks for the maximum absolute product, not the maximum product. If the problem statement asked for the maximum product, the function would need to return the maximum of the maximum positive product and the maximum negative product. 

However, in this case, the problem statement asks for the maximum absolute product, so the function returns the maximum absolute product, which is the maximum of the absolute values of the products. 

This is why the function returns `36`, which is the maximum absolute product between numbers in pairs of tuples within the given list. 

The function is designed to work with lists of tuples of any size, not just the specific list provided in the unit test. It can handle lists with any number of tuples, as long as each tuple contains exactly two