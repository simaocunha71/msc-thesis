```
def is_sublist(lst1, lst2):
    if not lst2:
        return True
    for i in range(len(lst1) - len(lst2) + 1):
        if lst1[i:i+len(lst2)] == lst2:
            return True
    return False
```





The function checks whether a list contains a given sublist or not. It iterates over the list and checks if the sublist is present at each position. If the sublist is found, the function returns True. If the sublist is not found after checking all positions, the function returns False. The function also handles the case where the sublist is empty by returning True in this case, as an empty sublist is considered to be contained in any list. The unit test `assert is_sublist([2,4,3,5,7],[3,7])==False` helps to clarify the problem by showing that the function should return False for a sublist that is not fully contained in the list.