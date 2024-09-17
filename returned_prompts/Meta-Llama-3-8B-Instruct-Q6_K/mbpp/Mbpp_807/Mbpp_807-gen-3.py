```
def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
    return None
```


The function iterates over the list of numbers. If it finds an odd number (i.e., a number that leaves a remainder when divided by 2), it returns that number. If it doesn't find any odd numbers, it returns None. 

The unit test `assert first_odd([1,3,5]) == 1` ensures that the function returns the first odd number in the list. If the list is empty, the function will return None, which is the expected behavior according to the problem statement. 

This function is case sensitive and will return the first odd number it encounters. If there are multiple odd numbers at the same index, it will return the first one it encounters. For example, `first_odd([1,3,1])` will return `1`, not `3`. 

The time complexity of this function is O(n), where n is the number of elements in the list, because it needs to iterate over the entire list to find the first odd number. The space complexity is O(1), because it only uses a constant amount of space to store the current number being examined. 





