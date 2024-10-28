```
def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return lst[i + 1]
    return None
```


Explanation:
The function `next_smallest` takes a list of integers as input. 
First, it checks if the list has less than 2 elements. If it does, the function returns `None` as there is no 2nd smallest element.
If the list has 2 or more elements, it sorts the list in ascending order. 
Then, it iterates over the list. If it finds an element that is smaller than the next element, it returns the next element, which is the 2nd smallest element.
If the loop finishes without finding such an element, it means the list is either sorted in ascending order or has all the same elements. In this case, the function returns `None`. 

This function works correctly for the given test cases. For example, `next_smallest([1, 2, 3, 4, 5])` returns `2`, `next_smallest([5, 1, 4, 3, 2])` returns `2`, `next_smallest([])` returns `None`, `next_smallest([1, 1])` returns `None`. 