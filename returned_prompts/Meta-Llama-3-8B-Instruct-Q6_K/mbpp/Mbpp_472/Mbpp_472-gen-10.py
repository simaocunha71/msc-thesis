```
def check_Consecutive(lst):
    for i in range(len(lst)-1):
        if abs(lst[i+1]-lst[i])>1:
            return False
    return True
```


This function iterates over the list and checks if the absolute difference between each pair of consecutive elements is greater than 1. If it finds such a pair, it immediately returns False, indicating that the list is not consecutive. If it doesn't find any such pair after checking the entire list, it returns True, indicating that the list is consecutive. 

The unit test `assert check_Consecutive([1,2,3,4,5]) == True` ensures that the function correctly identifies consecutive numbers in the list. 





```
print(check_Consecutive([1,2,3,4,5])) # Should print: True
print(check_Consecutive([1,2,4,5])) # Should print: False
```

Output:
```
True
False
```


This function is case sensitive and will return False if the list contains numbers that are not consecutive in the given order. For example, the list [1,3,4,5] would return False because the number 2 is missing. If you want to check for consecutive numbers regardless of order, you would need to sort the list first. 

Here's an updated function that checks for consecutive numbers regardless of order:
```
def check_Consecutive(lst):
    lst.sort()
    for i in range(len(lst)-1):
        if abs(lst[i+1]-lst[i])>1:
            return False
    return True
```
This function first sorts the list, then checks for consecutive numbers. It will return True if the list contains consecutive numbers, and False otherwise. For example, the list [1,3,4,5] would return True because the numbers are consecutive in the sorted list.