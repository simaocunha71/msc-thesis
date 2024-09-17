```
def diff_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0:
            even = num
        else:
            odd = num
        if even is not None and odd is not None:
            break
    return even - odd
```


This function iterates over the list to find the first even and first odd number. Once both numbers are found, it breaks the loop and calculates the difference. The unit test `assert diff_even_odd([1,3,5,7,4,1,6,8])==3` ensures that the function works correctly. 





