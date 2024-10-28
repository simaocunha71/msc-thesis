```
import math

def sum_squares(lst):
    return sum(math.ceil(i)**2 for i in lst)
```
The provided Python function `sum_squares` takes a list of numbers as input, squares each number, rounds each number to the upper integer using the `math.ceil` function, and then returns the sum of the squared and rounded numbers. 

The function uses a generator expression to square and round each number in the list, and the `sum` function to calculate the sum of the squared and rounded numbers. 

For example, if the input list is `[1, 2, 3]`, the function will calculate `math.ceil(1)**2 = 1**2 = 1`, `math.ceil(2)**2 = 2**2 = 4`, and `math.ceil(3)**2 = 3**2 = 9`, and then return `1 + 4 + 9 = 14`. 

This function works for both integer and floating-point numbers in the input list, and it handles negative numbers correctly. 

The time complexity of this function is O(n), where n is the length of the input list, because it needs to iterate over each element in the list once. The space complexity is O(1), because it only uses a constant amount of space to store the sum and the current number being processed. 