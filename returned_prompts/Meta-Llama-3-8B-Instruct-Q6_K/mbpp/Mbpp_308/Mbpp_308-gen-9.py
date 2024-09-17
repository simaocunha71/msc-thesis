```
def large_product(list1, list2, n):
    products = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            products.append(list1[i] * list2[j])
    return sorted(products, reverse=True)[:n]
```


The function `large_product` takes two lists and an integer `n` as input. It generates all possible products by combining one element from each list, stores them in a list, and then returns the `n` largest products. The unit test provided ensures that the function works correctly for the given input. 

For example, the input `([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)` would return `[60, 54, 50]`, which are the three largest products from the given lists. 

This function has a time complexity of O(m*n), where m and n are the lengths of the input lists. This is because it generates all possible products, which is a quadratic operation. The space complexity is also O(m*n), as it needs to store all the products in a list. 

Note that the input lists are not sorted, so the function needs to sort the products before returning the `n` largest ones. This is done using the `sorted` function with the `reverse=True` argument, which sorts the list in descending order. The `[:n]` slice is then used to return only the first `n` elements of the sorted list. 





Note: The problem statement asks for the specified number of largest products from two given lists, selecting one factor from each list. 

The unit test provided ensures that the function works correctly for the given input. 

This function has a time complexity of O(m*n), where m and n are the lengths of the input lists. 

The space complexity is also O(m*n), as it needs to store all the products in a list. 

The function sorts the products in descending order and then returns the first n elements of the sorted list. 

The function can be optimized by using a heap data structure to keep track of the n largest products as they are generated, instead of sorting the entire list. This would reduce the time complexity to O(m log n). However, the current implementation is simple and easy to understand.