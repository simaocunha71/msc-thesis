```
def min_product_tuple(lst):
    return min(a*b for a, b in lst)
```
The function `min_product_tuple` takes a list of tuples as an argument. It uses a generator expression to calculate the product of each pair of numbers in the list, and then returns the minimum of these products. The unit test `assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8` ensures that the function works correctly. 

For example, for the input `[(2, 7), (2, 6), (1, 8), (4, 9)]`, the function would return `8`, which is the minimum product of the pairs `(1, 8)` and `(2, 6)`. 

This function assumes that the input list contains tuples of two numbers. If the list can contain tuples of different lengths, the function would need to be modified to handle this case. 

The time complexity of this function is O(n), where n is the number of tuples in the list, because it needs to iterate over each tuple in the list once. The space complexity is O(1), because it only uses a constant amount of space to store the minimum product. 