The problem is asking to create a function that checks if a given list contains a specific sublist. However, the problem does not specify if the sublist should be contiguous or not. 

From the unit test provided, `assert is_sublist([2,4,3,5,7],[3,7])==False`, we can infer that the sublist should be contiguous. 

Here is a Python solution for the problem:

```
def is_sublist(lst, sublst):
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
```

This function first checks if the length of the sublist is greater than the length of the list. If it is, it immediately returns False. Then, it iterates over the list and checks if the sublist is present at any position. If it finds the sublist, it returns True. If it doesn't find the sublist after checking all positions, it returns False. 

This function assumes that the sublist is contiguous. If the sublist can be non-contiguous, the problem becomes more complex and requires a different approach. 












