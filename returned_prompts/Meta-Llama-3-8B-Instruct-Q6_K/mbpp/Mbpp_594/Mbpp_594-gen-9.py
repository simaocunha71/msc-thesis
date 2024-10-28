```
def diff_even_odd(lst):
    even = next((num for num in lst if num % 2 == 0), None)
    odd = next((num for num in lst if num % 2 != 0), None)
    if even is None or odd is None:
        return None
    return even - odd
```


The function `diff_even_odd` takes a list of numbers as input and returns the difference between the first even number and the first odd number in the list. If the list does not contain any even or odd numbers, the function returns `None`.

The function uses list comprehension to create iterators that yield the first even and odd numbers in the list. The `next` function is used to get the next value from these iterators.

The `if` statement checks if the list contains any even or odd numbers. If not, the function returns `None`. Otherwise, it returns the difference between the first even and odd numbers. 

This function passes the given unit test:
```
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
```


This test case checks if the function correctly calculates the difference between the first even and first odd numbers in the given list. The expected output is `3`, which is the difference between `4` (the first even number) and `1` (the first odd number) in the list. 














