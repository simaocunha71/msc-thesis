```
def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j+1):
                prod *= lst[k]
            total_sum += prod
    return total_sum
```
This function calculates the sum of products of all possible sublists of a given list. It does this by iterating over the list and for each sublist, it calculates the product of the elements and adds it to the total sum. The time complexity of this function is O(n^3) where n is the length of the input list. This is because for each element in the list, it calculates the product of all sublists ending at that element, which takes O(n) time. Therefore, the total time complexity is O(n^3). The space complexity is O(1) as it only uses a constant amount of space to store the variables. 

The unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` ensures that the function works correctly. The expected output is 20, which is the sum of products of all possible sublists of the list [1,2,3]. The sublists and their products are: [1] = 1, [2] = 2, [3] = 3, [1,2] = 2, [1,3] = 3, [2,3] = 6, [1,2,3] = 6. The sum of these products is 20. 

This function can be optimized by using dynamic programming to reduce the time complexity. However, the given function is simple and easy to understand. It is suitable for small input lists. For large input lists, a more optimized function would be necessary. 





Please let me know if you have any questions or if you'd like me to explain anything further.