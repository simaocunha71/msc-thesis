```
def max_product_tuple(tuples):
    max_product = 0
    for tuple in tuples:
        for i in range(len(tuple)):
            for j in range(len(tuple)):
                if i != j:
                    product = abs(tuple[i] * tuple[j])
                    if product > max_product:
                        max_product = product
    return max_product
```


The problem asks to find the maximum absolute product between numbers in pairs of tuples within a given list. 

The provided unit test `assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36` helps to understand that the problem is asking for the maximum absolute product of any pair of elements in the tuples. 

The function `max_product_tuple` iterates over each tuple and for each tuple, it generates all possible pairs of elements. It calculates the absolute product of each pair and keeps track of the maximum product found so far. 

The function returns the maximum product found. 

This solution has a time complexity of O(n^3) where n is the number of tuples, because it generates all possible pairs of elements and calculates the product for each pair. 

Please note that this solution assumes that the input list contains only tuples of integers. If the input list can contain other types of elements, additional error handling may be needed. 