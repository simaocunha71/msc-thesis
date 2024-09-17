```
def mul_even_odd(lst):
    even_nums = [num for num in lst if num % 2 == 0]
    odd_nums = [num for num in lst if num % 2 != 0]
    
    if not even_nums:
        return 0
    if not odd_nums:
        return 0
    
    return even_nums[0] * odd_nums[0]
```    
The function `mul_even_odd` takes a list of numbers as input and returns the product of the first even and odd number in the list. If the list contains no even or odd numbers, it returns 0. This function works by using list comprehensions to separate the even and odd numbers from the input list, and then returning the product of the first even and odd numbers. If either list is empty, it returns 0. This is checked by the unit test `assert mul_even_odd([1,3,5,7,4,1,6,8])==4`, which checks that the function returns the product of the first even and odd number in the list.