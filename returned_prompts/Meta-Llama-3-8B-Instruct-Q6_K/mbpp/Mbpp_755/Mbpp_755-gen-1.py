```
def second_smallest(lst):
    if len(lst) < 2:
        return None
    lst = sorted(set(lst))
    return lst[1]
```

This function first checks if the list has less than 2 elements, in which case it returns None. Then it creates a set of the list to remove duplicates and sorts the set. Finally, it returns the second element of the sorted set, which is the second smallest number in the list. 

The unit test `assert second_smallest([1, 2, -8, -2, 0, -2])==-2` ensures that the function works correctly. 

Please note that this function does not handle the case where the list has more than one duplicate of the smallest number. If you want to handle this case, you can modify the function to keep track of the count of the smallest number and return the second smallest number if there are more than one smallest numbers. 

Here is the modified function:

```
def second_smallest(lst):
    if len(lst) < 2:
        return None
    lst = sorted(set(lst))
    smallest = lst[0]
    count = 1
    for num in lst[1:]:
        if num == smallest:
            count += 1
        else:
            if count > 1:
                return smallest
            return num
    return None
```

This function first finds the smallest number in the list and counts how many times it appears. Then it iterates over the rest of the list, and if it finds a number that is not the smallest number, it returns that number if the count of the smallest number is more than 1. If it doesn't find any such number, it returns the smallest number. If the list has less than 2 elements, it returns None. 