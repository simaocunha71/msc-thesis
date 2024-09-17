```
def diff_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0:
            if even is None:
                even = num
        else:
            if odd is None:
                odd = num
    return even - odd
```
This function iterates over the list and keeps track of the first even and first odd numbers. If the number is even, it updates the `even` variable. If the number is odd, it updates the `odd` variable. Finally, it returns the difference between the two numbers. If the list contains no even or odd numbers, the function will return `None` - `None` which is `None`. The unit test `assert diff_even_odd([1,3,5,7,4,1,6,8])==3` ensures that the function works correctly. 

The time complexity of this function is O(n), where n is the length of the list, because it needs to iterate over the list once. The space complexity is O(1), because it uses a constant amount of space to store the variables `even` and `odd`. 