```
import math

def multiply_num(lst):
    result = 1
    for num in lst:
        result *= num
    return result / len(lst)
```
This function takes a list of numbers as input, multiplies all the numbers together, and then divides the result by the length of the list. The result is then returned. The `math.isclose` function is used in the unit test to check that the result is close to the expected value, within a certain tolerance. 

The unit test checks that the function returns the correct result for the input list `(8, 2, 3, -1, 7)`, which is `-67.2` to 3 decimal places. The `rel_tol` parameter in the `math.isclose` function specifies the relative tolerance, which is 0.001 in this case. This means that the result is considered correct if it is within 0.1% of the expected value. 

The function works by initializing a variable `result` to 1, then iterating over each number in the input list. For each number, it multiplies the current value of `result` by the number. After all numbers have been processed, it returns the final value of `result` divided by the length of the input list. 

For example, if the input list is `(8, 2, 3, -1, 7)`, the function will multiply the numbers together to get `8 * 2 * 3 * -1 * 7 = -168`, then divide by the length of the list `5` to get `-33.6`. The result is then returned. 

Note that this function assumes that the input list is not empty. If the input list is empty, the function will raise a ZeroDivisionError when it tries to divide by the length of the list. You may want to add error handling to handle this case if necessary. 

Also, this function uses the `math.isclose` function from the math module to check that the result is close to the expected value. This function is used to compare floating point numbers, which can have small rounding errors. The `math.isclose` function takes two arguments, `a` and `b`, and returns `True` if `a` and `b` are close to each other, within a certain tolerance. The `rel_tol` parameter specifies the relative tolerance, which is the maximum allowed difference between `a` and `b` as a fraction