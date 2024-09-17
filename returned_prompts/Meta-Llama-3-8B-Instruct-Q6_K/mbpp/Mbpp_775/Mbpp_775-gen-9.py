```
def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True
``` 

Explanation:
The function `odd_position` iterates over the list with a step of 2, starting from the second element (index 1). It checks if each element at an odd index is odd by using the modulus operator `%`. If it finds an even number, it immediately returns `False`. If it goes through all elements without finding an even number, it returns `True`. 

The unit test `assert odd_position([2,1,4,3,6,7,6,3]) == True` ensures that the function works correctly. In this case, every odd index (1, 3, 5, 7) contains an odd number, so the function returns `True`. 

This function assumes that the input list is not empty. If the list can be empty, you might want to add a check for that at the beginning of the function. 