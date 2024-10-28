You can solve this problem by using a set to remove duplicate numbers. Here is the Python function for it:

```Python
def two_unique_nums(lst):
    return list(set([i for i in lst if lst.count(i) == 1]))
```
This function uses a list comprehension to create a list of unique numbers from the input list. The set function is used to remove duplicate numbers. The list comprehension also includes a condition to only include numbers that appear only once in the list. The result is converted back to a list before being returned.

For example, if you call `two_unique_nums([1,2,3,2,3,4,5])`, it will return `[1, 4, 5]`. This is because 1, 4, and 5 are the only numbers that appear only once in the input list. 

This function has a time complexity of O(n^2) because the count function has a time complexity of O(n). This could be inefficient for large lists. A more efficient solution would be to use a dictionary to count the occurrences of each number, which would have a time complexity of O(n). 

Here is the more efficient solution:

```Python
def two_unique_nums(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return [num for num, freq in count.items() if freq == 1]
```  This function has a time complexity of O(n) and a space complexity of O(n). It is more efficient than the previous solution for large lists. 