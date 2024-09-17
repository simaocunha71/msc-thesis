```
def diff_even_odd(lst):
    even = next((x for x in lst if x % 2 == 0), None)
    odd = next((x for x in lst if x % 2 != 0), None)
    if even is None or odd is None:
        return None
    return abs(even - odd)
```
This function uses list comprehension to find the first even and odd number in the list. If neither an even nor an odd number is found, it returns `None`. Otherwise, it returns the absolute difference between the two numbers. The unit test `assert diff_even_odd([1,3,5,7,4,1,6,8])==3` ensures that the function works correctly. 





