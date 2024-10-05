You can use a list comprehension to square each number in the list, round each number to the upper int using the math.ceil function, and then sum the results. Here is the Python code for it:

```Python
import math
def sum_squares(lst):
    return sum(math.ceil(i)**2 for i in lst)
```

This function will return the sum of the squares of the numbers in the list, after each number is rounded to the upper integer using the math.ceil function. For example, if you call `sum_squares([1,2,3])`, it will return 14, which is the sum of the squares of 2 and 3 (1 is rounded to 1, so its square is 1). If you call `sum_squares([1,4,9])`, it will return 98, which is the sum of the squares of 2, 5, and 10 (1 is rounded to 2, 4 is rounded to 5, and 9 is rounded to 10). 

This function can be called with a list of numbers as the argument, such as `sum_squares([1,2,3])` or `sum_squares([-2.4,1,1])`. It will return the sum of the squares of the numbers in the list, after each number is rounded to the upper integer.