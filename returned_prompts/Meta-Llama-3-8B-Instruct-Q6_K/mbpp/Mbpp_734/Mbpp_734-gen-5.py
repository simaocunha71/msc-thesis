```
def sum_Of_Subarray_Prod(lst):
    prod = 1
    for i in range(len(lst)):
        prod *= lst[i]
    total_sum = prod
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            subarray = lst[i:j]
            prod = 1
            for num in subarray:
                prod *= num
            total_sum += prod
    return total_sum
```
Explanation: 
The function calculates the sum of products of all possible sublists of a given list. It first calculates the product of the entire list. Then, it iterates over the list to generate all possible sublists, calculates the product of each sublist, and adds it to the total sum. The function returns the total sum. 

Note: The unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` suggests that the problem is asking for the sum of products of all possible sublists, not just the maximum or minimum subarray product. Therefore, we need to calculate the product of each sublist and add it to the total sum. 

The time complexity of this function is O(n^2 * n), where n is the length of the input list. This is because we are iterating over the list to generate all possible sublists, and for each sublist, we are calculating its product. The space complexity is O(n), where n is the length of the input list. This is because we are storing the entire list and the sublists in memory. 

This function may not be efficient for large input lists due to its high time complexity. For a more efficient solution, we could use dynamic programming to calculate the product of each sublist in O(n) time. However, this would make the function more complex and harder to understand. 