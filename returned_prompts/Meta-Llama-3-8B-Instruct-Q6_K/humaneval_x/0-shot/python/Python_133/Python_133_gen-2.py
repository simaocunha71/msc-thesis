```
def sum_squares(lst):
    return sum(math.ceil(x)**2 for x in lst)
```
This function uses a generator expression to iterate over the input list, round each element to the upper int using `math.ceil`, square the result, and sum up all the squared values. The `math.ceil` function is used to round each element to the upper int. 

For example, for the input list `[1,2,3]`, the function will calculate the sum of squared values as follows: 
- `math.ceil(1)` is 1, `1**2` is 1, 
- `math.ceil(2)` is 2, `2**2` is 4, 
- `math.ceil(3)` is 3, `3**2` is 9.
Then it will sum up these values: `1+4+9=14`. 

So, the output for the input list `[1,2,3]` will be `14`. 

The `math.ceil` function is used to round each element to the upper int. This is necessary because the problem statement requires rounding each element to the upper int before squaring. 

The `sum` function is used to calculate the sum of the squared values. The generator expression `(math.ceil(x)**2 for x in lst)` is used to iterate over the input list, round each element to the upper int, square the result, and sum up all the squared values. 

The function returns the sum of the squared values. 

This function will work correctly for any input list of numbers, including negative numbers and non-integer numbers. 