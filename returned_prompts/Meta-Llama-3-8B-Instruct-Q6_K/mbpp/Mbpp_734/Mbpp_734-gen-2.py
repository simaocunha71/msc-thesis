```
def sum_Of_Subarray_Prod(lst):
    total_sum = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            total_sum += sum([lst[k] for k in range(i, j+1)])
    return total_sum
```
This function uses two nested loops to generate all possible sublists of the given list. It then calculates the sum of products of each sublist by summing the elements in the sublist. The total sum of all these sums is the final result. 

For example, for the list [1,2,3], the function will calculate the sum of products of the following sublists: [1], [1,2], [1,2,3], [2], [2,3], [3], which are [1], [1+2], [1+2+3], [2], [2+3], [3] respectively, and return the total sum 20. 

Note that this function has a time complexity of O(n^3) due to the three nested loops, where n is the length of the input list. This may not be efficient for large lists. 

The unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` ensures that the function returns the correct result for the list [1,2,3]. 

Please note that this problem is not well-defined for empty lists, as the sum of products of the empty list is undefined. You may want to add a special case to handle this situation. 