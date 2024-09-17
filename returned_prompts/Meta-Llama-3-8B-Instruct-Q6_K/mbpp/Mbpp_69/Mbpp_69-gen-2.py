```
def is_sublist(lst, sublst):
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst)):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
```


```
def is_sublist(lst, sublst):
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst)):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
```


This function checks if a given sublist exists in a list. It first checks if the length of the sublist is greater than the length of the list. If it is, it immediately returns False because the sublist cannot exist in the list.

Then, it iterates over the list and checks if the sublist exists at each position in the list. If it finds the sublist at any position, it returns True. If it doesn't find the sublist at any position, it returns False.

For example, `is_sublist([2,4,3,5,7], [3,7])` returns False because the sublist [3,7] is not in the list. But `is_sublist([2,4,3,5,7], [3])` returns True because the sublist [3] is in the list. The unit test `assert is_sublist([2,4,3,5,7],[3,7])==False` also passes. 

This function has a time complexity of O(n*m) where n is the length of the list and m is the length of the sublist. This is because in the worst case, it has to iterate over the list and the sublist for each position in the list. 

This function also has a space complexity of O(1) because it only uses a constant amount of space to store the indices and the sublist. 

The function can be optimized by returning as soon as it finds the sublist. This would reduce the time complexity to O(n) in the best case, but it would still be O(n*m) in the worst case. 

The function can also be optimized by using a sliding window approach, where it only checks if the sublist exists at each position in the list once. This would reduce the time complexity to O(n) in the worst case. 

Here is the optimized function:

```
def is_sublist(lst, sublst):
    if len(sublst) > len(lst):
       