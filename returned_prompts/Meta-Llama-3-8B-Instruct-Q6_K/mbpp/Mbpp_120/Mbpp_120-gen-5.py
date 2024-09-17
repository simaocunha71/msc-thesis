```
def max_product_tuple(lst):
    max_product = float('-inf')
    for num1, num2 in lst:
        product = abs(num1 * num2)
        if product > max_product:
            max_product = product
    return max_product
```


This function iterates over the list of tuples, calculates the absolute product of each pair of numbers, and keeps track of the maximum product found. The absolute value is used to ensure that the product is calculated correctly regardless of the order of the numbers in the pair. The function returns the maximum product found. 

For example, given the list `[(2, 7), (2, 6), (1, 8), (4, 9)]`, the function will return `36`, which is the maximum absolute product between numbers in pairs of tuples within the list. 





