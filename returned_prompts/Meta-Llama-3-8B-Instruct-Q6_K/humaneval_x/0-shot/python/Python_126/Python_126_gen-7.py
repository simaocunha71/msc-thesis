```
def is_sorted(lst):
    if len(lst) <= 1:
        return True

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        elif lst[i] == lst[i + 1]:
            for j in range(i + 1, len(lst) - 1):
                if lst[j] < lst[j + 1]:
                    return False
            return False

    return True
```


This function takes a list of numbers as input and checks if they are sorted in ascending order. If there are more than one duplicate of the same number, it returns False. 

The function first checks if the list has less than or equal to one element. If so, it returns True as a list with less than or equal to one element is automatically sorted.

Then, it iterates over the list. If it finds a pair of adjacent elements where the first element is greater than the second, it immediately returns False.

If it finds a pair of adjacent elements where the first element is equal to the second, it checks the rest of the list to see if there are any other adjacent elements that are not in order. If it finds any, it returns False. If it doesn't find any, it returns False anyway because the list has more than one duplicate of the same number.

If the function doesn't find any pairs of adjacent elements that are not in order, it returns True. 

This function works for lists of integers and does not handle negative numbers or non-integer values. It also assumes that the list does not contain any duplicate numbers. If the list can contain negative numbers or non-integer values, or if it can contain duplicate numbers, the function would need to be modified accordingly. 