```
def sum_Of_Subarray_Prod(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            result += prod(lst[i:j+1])
    return result

def prod(lst):
    res = 1
    for num in lst:
        res *= num
    return res
```
This function first defines a helper function `prod` to calculate the product of a list of numbers. Then it iterates over all possible sublists of the input list `lst`, calculates the product of each sublist, and adds it to the result. The result is the sum of products of all possible sublists of the input list.

The unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` suggests that the function should return 20 when the input list is [1,2,3]. This can be achieved by calculating the product of all possible sublists of [1,2,3], which are [1], [1,2], [1,2,3], [2], [2,3], [3], and summing them up. The product of each sublist is 1, 2, 6, 2, 6, 3, respectively, and their sum is 20. 

Note that this function has a time complexity of O(n^3), where n is the length of the input list, because it iterates over all possible sublists and calculates the product of each sublist. This may not be efficient for large input lists. 