```
def second_smallest(lst):
    lst = list(set(lst))
    if len(lst) < 2:
        return None
    return sorted(lst)[1]
```


The problem is asking to create a function that finds the second smallest number in a given list. 

The provided unit test `assert second_smallest([1, 2, -8, -2, 0, -2])==-2` helps to clarify the problem by showing that the function should return the second smallest number, even if the list has duplicate numbers.

Here is the solution:

The function first removes duplicate numbers from the list by converting it to a set and then back to a list. If the list now has less than 2 elements, it means that the original list had only one unique number, so the function returns None. Otherwise, it sorts the list and returns the second element, which is the second smallest number.

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the number of elements in the list. The space complexity is O(n) for storing the set and the sorted list. 