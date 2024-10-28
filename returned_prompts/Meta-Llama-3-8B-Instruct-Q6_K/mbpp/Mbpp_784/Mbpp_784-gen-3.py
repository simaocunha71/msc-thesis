```
def mul_even_odd(lst):
    even = [i for i in lst if i % 2 == 0]
    odd = [i for i in lst if i % 2 != 0]
    return even[0] * odd[0]
```
The function takes a list as input and returns the product of the first even and odd numbers in the list. The function uses list comprehensions to create lists of even and odd numbers, and then returns the product of the first elements of these lists. 

The unit test `assert mul_even_odd([1,3,5,7,4,1,6,8])==4` ensures that the function works correctly. It checks if the product of the first even and odd numbers in the list `[1,3,5,7,4,1,6,8]` is `4`, which is the correct result. 





