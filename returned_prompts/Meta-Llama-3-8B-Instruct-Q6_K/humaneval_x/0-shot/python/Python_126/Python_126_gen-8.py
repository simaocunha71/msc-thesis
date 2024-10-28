```
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            if lst.count(lst[i]) > 1:
                return False
    return True
```

This function iterates over the list, checking if each element is less than or equal to the next one. If it finds a pair of elements where the first one is not less than the second one, it checks if the first element has any duplicates. If it does, the function returns `False`, indicating that the list is not sorted. If it doesn't find any such pairs or if the first element has no duplicates, it returns `True`, indicating that the list is sorted. 

The `count` method of the list is used to count the occurrences of an element. This is used to check if the element has any duplicates. 

Note: This function assumes that the list does not contain any negative numbers and only integers. If the list can contain negative numbers or non-integer values, additional checks would be needed. 

Also, this function has a time complexity of O(n^2) due to the use of the `count` method, which has a time complexity of O(n). If the list is large, this function may be slow. A more efficient solution would be to use a dictionary to keep track of the counts of each element, which would have a time complexity of O(n). 

Here is an example of how you could use a dictionary to keep track of the counts of each element:
```
def is_sorted(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True
```
This version of the function has a time complexity of O(n), making it more efficient for large lists. 

However, the original function is simpler and may be more readable for some people, so it's up to you to decide which one to use. 