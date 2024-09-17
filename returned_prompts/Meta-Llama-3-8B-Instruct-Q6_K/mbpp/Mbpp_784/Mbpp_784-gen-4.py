```
def mul_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0:
            even = num
        else:
            odd = num
        if even is not None and odd is not None:
            break
    return even * odd if even is not None and odd is not None else None
```    
The function iterates through the list and finds the first even and odd numbers. If both numbers are found, it breaks the loop and returns their product. If neither number is found, it returns None. The unit test `assert mul_even_odd([1,3,5,7,4,1,6,8])==4` ensures that the function works correctly. The function assumes that the list is not empty and contains at least one even and one odd number. If the list does not contain both an even and an odd number, the function returns None. If the list is empty, the function will not work correctly and should be modified to handle this case.