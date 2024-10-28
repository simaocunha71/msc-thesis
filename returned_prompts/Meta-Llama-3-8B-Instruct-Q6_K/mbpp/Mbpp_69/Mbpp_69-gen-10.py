```
def is_sublist(lst1, lst2):
    if not lst2:
        return True
    for i in range(len(lst1)-len(lst2)+1):
        if lst1[i:i+len(lst2)] == lst2:
            return True
    return False
```
This function checks if a sublist exists in a list. It iterates over the list and checks if the sublist matches at each position. If the sublist matches at any position, the function returns True. If the sublist does not match at any position, the function returns False. The function also handles the case where the sublist is an empty list. In this case, the function returns True because an empty list is considered a sublist of any list.

The unit test `assert is_sublist([2,4,3,5,7],[3,7])==False` ensures that the function correctly returns False when the sublist is not found in the list. This test is important because it checks the function's behavior when the sublist is not found, which is a common edge case. 





