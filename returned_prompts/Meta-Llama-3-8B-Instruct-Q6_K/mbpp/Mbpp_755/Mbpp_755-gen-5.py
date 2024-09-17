```
def second_smallest(lst):
    lst = list(set(lst))  # remove duplicates
    lst.sort()
    return lst[1]
```
The function first removes duplicates from the list by converting it to a set and back to a list. Then it sorts the list. Finally, it returns the second element of the sorted list, which is the second smallest number. This solution assumes that the list has at least two elements. If the list has only one element, it will raise an IndexError when trying to access the second element. If the list is empty, it will raise a ValueError when trying to convert the empty list to a set. 

The unit test `assert second_smallest([1, 2, -8, -2, 0, -2])==-2` suggests that the function should return the second smallest number in the list, which is -2. 

This solution is efficient because it has a time complexity of O(n log n) due to the sorting operation, where n is the number of elements in the list. The space complexity is O(n) because it needs to store the sorted list. 