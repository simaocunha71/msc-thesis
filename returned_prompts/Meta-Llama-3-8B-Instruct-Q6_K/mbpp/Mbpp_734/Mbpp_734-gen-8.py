```
def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total_sum = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= lst[j]
            total_sum += prod
    return total_sum
```


The function `sum_Of_Subarray_Prod` calculates the sum of products of all possible sublists of a given list. It iterates over each element in the list and calculates the product of all elements starting from that point to the end of the list. This product is then added to the total sum. 

For example, given the list [1,2,3], the function will calculate the sum of products of all possible sublists: [1], [1,2], [1,2,3], [2], [2,3], [3], which is 1 + 1*2 + 1*2*3 + 2 + 2*3 + 3 = 20. 

The unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` confirms that the function works correctly for this example. 





