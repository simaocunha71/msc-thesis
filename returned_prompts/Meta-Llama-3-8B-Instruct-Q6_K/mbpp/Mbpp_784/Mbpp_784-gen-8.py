```
def mul_even_odd(lst):
    even = next((x for x in lst if x % 2 == 0), None)
    odd = next((x for x in lst if x % 2 != 0), None)
    return even * odd if even and odd else None
```


The function `mul_even_odd` takes a list of numbers as input. It uses list comprehension to find the first even and odd number in the list, and then returns their product. If no even or odd number is found, the function returns `None`. The unit test provided ensures that the function works correctly. For example, when the input list is `[1,3,5,7,4,1,6,8]`, the function should return `4`, which is the product of the first even number `4` and the first odd number `1`. If the input list contains no even or odd number, the function will return `None`. 

The unit test `assert mul_even_odd([1,3,5,7,4,1,6,8])==4` ensures that the function works correctly for this specific input. 

The function uses the `next` function with a generator expression to find the first even and odd number in the list. The `next` function returns the first item from the iterable for which the function returns `True`. If no such item is found, it returns `None`. 

The function also includes a check to return `None` if no even or odd number is found. This is to ensure that the function does not raise an error when the input list contains no even or odd number. 

The function is designed to work with any list of numbers, not just the specific input provided in the unit test. It can handle lists with no even or odd numbers, and it returns `None` in such cases. 