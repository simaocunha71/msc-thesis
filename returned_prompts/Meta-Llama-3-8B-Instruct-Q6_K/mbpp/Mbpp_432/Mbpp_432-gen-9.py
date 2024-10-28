The problem is asking to write a function that calculates the median length of a trapezium. The trapezium's length is given by the formula: (a+b)/2, where a and b are the lengths of the two parallel sides.

However, the problem doesn't specify the lengths of the parallel sides. But, we can solve the problem by assuming the lengths of the parallel sides are given as input to the function. This is also supported by the unit test `assert median_trapezium(15,25,35)==20`, which suggests that the function should take three parameters.

Here is the solution:
```
def median_trapezium(a, b, c):
    return (a+b)/2
```
This function takes three parameters `a`, `b`, and `c`, which are the lengths of the parallel sides. It returns the median length of the trapezium, which is the average of the lengths of the parallel sides. The unit test `assert median_trapezium(15,25,35)==20` passes with this function.