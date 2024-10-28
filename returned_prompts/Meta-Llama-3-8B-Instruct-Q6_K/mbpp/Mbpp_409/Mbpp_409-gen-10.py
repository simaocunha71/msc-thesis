```
def min_product_tuple(lst):
    products = [t[0] * t[1] for t in lst]
    return min(products)
```
The function `min_product_tuple` takes a list of tuples as input. It calculates the product of each tuple and stores them in a list called `products`. Then, it returns the minimum product from the list. This function can be used to find the minimum product from the pairs of tuples within a given list, as shown in the unit test. 

The unit test `assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8` ensures that the function works correctly by comparing the output of the function with the expected result. 

For example, given the list `[(2, 7), (2, 6), (1, 8), (4, 9)]`, the function will calculate the products as `[14, 12, 8, 36]` and return the minimum product `8`. 

This function assumes that the input list is not empty and each tuple in the list has exactly two elements. If these assumptions are not valid, additional error checking and handling may be necessary. 