```
def is_sublist(lst, sublst):
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst)):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
```
This function checks if a given sublist is present in a list. It first checks if the length of the sublist is greater than the length of the list. If it is, it returns False as the sublist cannot be present in the list.

Then it iterates over the list and checks if the sublist is present at any position in the list. If it finds the sublist, it returns True. If it does not find the sublist after checking all positions, it returns False. 