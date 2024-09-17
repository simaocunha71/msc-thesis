The problem is asking to find the sum of products of all possible sublists of a given list. 

For example, if the list is [1, 2, 3], the problem is asking to find the sum of products of all possible sublists such as [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3].

However, the problem description does not specify what to do with the empty sublist. 

Luckily, the unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` gives us a hint. It suggests that we should include the empty sublist in our calculation. 

Here is a Python function that solves the problem:

```
def sum_Of_Subarray_Prod(lst):
    total = 0
    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            total += math.prod(lst[i:j])
    return total
```

In this function, we are iterating over all possible sublists of the given list and calculating the product of each sublist. We are then summing up all these products to get the total sum. 

The `math.prod` function is used to calculate the product of a list. This function is available in Python 3.8 and later versions. For earlier versions, you can use the `functools.reduce` function with the `operator.mul` function to achieve the same result. 

Please note that this function has a time complexity of O(n^3) due to the nested loops and the `math.prod` function. It may not be efficient for large lists. 