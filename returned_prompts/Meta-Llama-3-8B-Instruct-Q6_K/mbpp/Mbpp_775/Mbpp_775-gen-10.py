```
def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True
```
This function iterates over the list with a step of 2, starting from the first odd index (1). It checks each element at the odd index if it's even. If it finds an even number, it returns False. If it doesn't find any even numbers, it returns True.

The unit test `assert odd_position([2,1,4,3,6,7,6,3]) == True` is used to ensure the function is working correctly. It checks if the function returns True for the given list, which means every odd index contains odd numbers in the list. 