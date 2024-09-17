```
def mul_even_odd(lst):
    even = [num for num in lst if num % 2 == 0]
    odd = [num for num in lst if num % 2 != 0]
    if len(even) == 0 or len(odd) == 0:
        return None
    return even[0] * odd[0]
```





# test
print(mul_even_odd([1,3,5,7,4,1,6,8]))  # Output: 4
```







# Explanation:

The function `mul_even_odd` takes a list of numbers as input. It first filters the list to get all even numbers and all odd numbers. If either of the lists is empty (i.e., there are no even or odd numbers in the list), it returns `None`. Otherwise, it returns the product of the first even number and the first odd number.

The unit test `assert mul_even_odd([1,3,5,7,4,1,6,8])==4` checks that the function returns the correct result for the given input. In this case, the first even number is 4 and the first odd number is 1, so the product is 4.