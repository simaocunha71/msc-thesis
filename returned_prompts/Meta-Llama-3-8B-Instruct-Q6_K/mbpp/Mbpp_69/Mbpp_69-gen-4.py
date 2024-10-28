```
def is_sublist(lst, sublist):
    for i in range(len(lst)):
        if lst[i:i+len(sublist)] == sublist:
            return True
    return False
```
The function is_sublist checks if a given sublist is present in the main list. It iterates over the main list, slicing the list from the current position to the length of the sublist. If the sliced list is equal to the sublist, it returns True. If it doesn't find the sublist after checking all positions, it returns False. 

For example, if the main list is [2,4,3,5,7] and the sublist is [3,7], the function will return False because [3,7] is not present in the main list. 

However, the unit test `assert is_sublist([2,4,3,5,7],[3,7])==False` is incorrect. It should be `assert is_sublist([2,4,3,5,7],[2,4,3,5,7])==True` or `assert is_sublist([2,4,3,5,7],[2,4,3,5,7])==False` depending on whether the function should check for exact matches or consider sublists as equal if they have the same elements in any order. 

The function will return False for the unit test `assert is_sublist([2,4,3,5,7],[3,7])==False` because it checks for exact matches and [3,7] is not present in the main list. If the function should consider sublists as equal if they have the same elements in any order, it should return True for the unit test. 