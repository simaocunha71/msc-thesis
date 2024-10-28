```
def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
    return None
```


The function iterates through the list of numbers. If it finds an odd number (i.e., a number that is not divisible by 2), it returns that number. If the function iterates through the entire list without finding an odd number, it returns None. 

The provided unit test `assert first_odd([1,3,5]) == 1` ensures that the function works correctly for the given list. If the function is implemented correctly, the unit test will pass. 

This solution assumes that the input list is not empty. If the list can be empty, you might want to add a check for that at the beginning of the function and return None or a default value in that case. 

The time complexity of this function is O(n), where n is the number of elements in the list, because it needs to iterate through the entire list. The space complexity is O(1), because it only uses a constant amount of space to store the current number being processed. 