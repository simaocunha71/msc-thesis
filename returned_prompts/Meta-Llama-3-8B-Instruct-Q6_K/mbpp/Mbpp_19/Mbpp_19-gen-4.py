```
def has_duplicates(array):
    return len(array) != len(set(array))
```
This function works by converting the array into a set, which automatically removes any duplicate elements. It then compares the length of the original array to the length of the set. If the lengths are different, that means there were some duplicate elements in the array, and the function returns True. Otherwise, it returns False. 

For example, if we call `has_duplicates([1,2,3,4,5])`, it will return False because there are no duplicate elements in the array. If we call `has_duplicates([1,2,3,4,4])`, it will return True because there is a duplicate element (4) in the array. 

The unit test `assert test_duplicate(([1,2,3,4,5]))==False` ensures that the function works correctly for arrays without duplicates.  The test `assert test_duplicate([1,2,3,4,4])==True` ensures that the function works correctly for arrays with duplicates. 

Note that this function has a time complexity of O(n), where n is the number of elements in the array, because it needs to iterate over the array once to convert it to a set. The space complexity is also O(n), because in the worst case, the set will contain all the elements from the array.  Therefore, this function is efficient for large arrays.  However, it may not be the most efficient function for very large arrays, because converting the array to a set requires extra memory.  If memory is a concern, a more complex function with a lower space complexity may be needed.  For example, a function that only uses a constant amount of extra memory could be implemented using a hash table, but it would be more complex and harder to understand.  In general, the best approach will depend on the specific requirements of the problem.  In this case, the function provided is simple, efficient, and easy to understand, so it is a good choice. 