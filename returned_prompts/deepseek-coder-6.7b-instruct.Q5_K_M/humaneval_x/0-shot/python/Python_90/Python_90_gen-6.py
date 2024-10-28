
    # First, let's remove duplicates from the list
    lst = list(set(lst))
    
    # Then, sort the list in ascending order
    lst.sort()
    
    # Finally, return the second element if the list is long enough, otherwise return None
    return lst[1] if len(lst) >= 2 else None


print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 1, 4, 3, 2]))  # 2
print(next_smallest([]))  # None
print(next_smallest([1, 1]))  # None

# This code works by first removing duplicates from the list, then sorting the list in ascending order, and finally returning the second element of the list. If the list does not have at least two elements, the function returns None.

```


</div>



</div>

## Solution


```python
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    # First, let's remove duplicates from the list
    lst = list(set(lst))
    
    # Then, sort the list in ascending order
    lst.sort()
    
    # Finally, return the second element if the list is long enough, otherwise return None
    return lst[1] if len(lst) >= 2 else None


print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 