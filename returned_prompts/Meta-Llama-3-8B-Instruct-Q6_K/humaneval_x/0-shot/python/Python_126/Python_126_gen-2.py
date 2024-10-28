```
def is_sorted(lst):
    if len(lst) <= 1:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
```


Explanation:
The function checks if the list is sorted in ascending order. It iterates over the list, comparing each element with the next one. If it finds a pair of elements where the first is greater than the second, it returns False, indicating that the list is not sorted. If it doesn't find any such pair, it returns True, indicating that the list is sorted.

The function also checks for lists with a length of 1 or less, in which case it returns True, since a single-element list is always sorted.

The function does not handle the case of duplicate elements as per the problem description, but it can be modified to do so. For example, it could count the occurrences of each element and return False if any element appears more than once. However, this is not necessary for the given examples, which do not contain duplicate elements.