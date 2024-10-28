```
def min_product_tuple(tuples):
    min_product = float('inf')
    for pair in tuples:
        product = pair[0] * pair[1]
        if product < min_product:
            min_product = product
    return min_product
``` 

This function iterates over each tuple in the given list, calculates the product of the elements in each tuple, and keeps track of the minimum product found. The function returns the minimum product.

The unit test `assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8` confirms that the function works correctly, as the minimum product is 8, which is the product of the pair (1,8). 

The time complexity of this function is O(n), where n is the number of tuples in the list, as it iterates over each tuple once. The space complexity is O(1), as it uses a constant amount of space to store the minimum product. 