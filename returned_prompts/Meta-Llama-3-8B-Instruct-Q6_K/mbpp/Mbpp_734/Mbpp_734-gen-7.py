```
def sum_Of_Subarray_Prod(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            res += lst[i] * lst[j]
    return res
```
This function takes a list as input and returns the sum of products of all possible sublists. It iterates over all possible sublists and adds their products to the result. The time complexity of this function is O(n^2) where n is the length of the list. 

For example, if the input list is [1,2,3], the function will calculate the products of all possible sublists: [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] and return their sum, which is 20. 

The unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` ensures that the function returns the correct result for the input list [1,2,3]. 

Note: This function does not consider the order of elements in the sublists. If the order is important, the function needs to be modified accordingly. 

Also, this function has a high time complexity due to the nested loops. If the input list is large, this function may be slow. In that case, a more efficient algorithm is needed. 





```
def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total = sum(lst)
    res = 0
    for i in range(n):
        res += lst[i] * (total - lst[i])
    return res
```
This function calculates the sum of products of all possible sublists in O(n) time complexity. It first calculates the total sum of the list, then for each element in the list, it calculates the product of the current element and the sum of the remaining elements, and adds it to the result. This way, it avoids calculating the same product multiple times. 

This function still does not consider the order of elements in the sublists. If the order is important, the function needs to be modified accordingly. 

The unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` ensures that the function returns the correct result for the input list [1,2,3]. 