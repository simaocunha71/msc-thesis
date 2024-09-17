The problem is asking to write a function that counts the number of pairs of strings in a given list where each string is a reverse of the other. For example, "julia" and "ailuj" are a pair because "julia" is the reverse of "ailuj". 

Here is a Python solution for this problem:

```
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1] or lst[j] == lst[i][::-1]:
                count += 1
    return count
```

This function works by iterating over each string in the list and checking if it is a reverse of any other string in the list. If it is, it increments the count. The `[::-1]` is used to reverse a string in Python. 

For example, if the input list is `["julia", "best", "tseb", "for", "ailuj"]`, the function will return `2` because "julia" and "ailuj" are a pair and "tseb" and "best" are a pair. 

The unit test `assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2` also confirms that the function is working correctly. 





This solution has a time complexity of O(n^2) where n is the number of strings in the list, because it is using two nested loops to iterate over the list. This is not efficient for large lists. If the list is very large, a more efficient solution would be needed. 

However, for small to medium-sized lists, this solution should work fine. 