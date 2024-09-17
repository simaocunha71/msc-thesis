The problem is asking to find the median length of a trapezium. The given lengths are the lengths of the parallel sides of the trapezium. 

However, the problem doesn't specify whether the median should be calculated from the lengths of the parallel sides or from the lengths of the non-parallel sides.

Thanks to the unit test `assert median_trapezium(15,25,35)==20`, we can infer that the median should be calculated from the lengths of the parallel sides. 

The median of three numbers is the middle value when they are arranged in order. For three numbers, the median is the second number when they are arranged in order. 

Here is the Python function that solves the problem:
```
def median_trapezium(a, b, c):
    return sorted([a, b, c])[1]
``` 





Note: This solution assumes that the input lengths are valid (i.e., they are not negative and are not equal to each other). In a real-world scenario, you would need to add error checking code to handle these cases.