```
def mul_even_odd(lst):
    even = next((x for x in lst if x % 2 == 0), None)
    odd = next((x for x in lst if x % 2 != 0), None)
    if even is None or odd is None:
        return None
    return even * odd
```




The solution is written in Python. It defines a function `mul_even_odd(lst)` that takes a list of numbers `lst` as input and returns the product of the first even and odd number in the list. If there are no even or odd numbers in the list, it returns `None`.

The function uses list comprehension to find the first even and odd numbers in the list. The `next()` function is used to get the first matching element from the list, or `None` if no matching element is found.

In the unit test, the function is called with the list `[1,3,5,7,4,1,6,8]` and the expected output is `4`, which is the product of the first even number `4` and the first odd number `1`.