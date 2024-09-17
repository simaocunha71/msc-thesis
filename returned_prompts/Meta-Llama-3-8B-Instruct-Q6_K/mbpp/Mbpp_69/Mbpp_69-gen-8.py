```
def is_sublist(lst, sublst):
    if not isinstance(lst, list) or not isinstance(sublst, list):
        return False
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
```





This function checks whether a list contains a given sublist. It first checks if the input is a list. If not, it returns False. It then checks if the length of the sublist is greater than the length of the list, if so, it returns False. Finally, it iterates over the list and checks if the sublist is present at any position. If the sublist is found, it returns True, otherwise, it returns False.

The unit test `assert is_sublist([2,4,3,5,7],[3,7])==False` is used to check if the function correctly returns False when the sublist is not present in the list. This test helps to ensure that the function is working correctly.