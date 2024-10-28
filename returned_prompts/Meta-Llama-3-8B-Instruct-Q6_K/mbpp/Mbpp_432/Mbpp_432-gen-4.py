The problem is asking you to write a function that calculates the median length of a trapezium. The trapezium has three sides, and the function should return the median length of these sides.

Looking at the unit test provided, `assert median_trapezium(15,25,35)==20`, we can see that the function should take three parameters, representing the lengths of the three sides of the trapezium. The median length is then the middle value when the sides are sorted in ascending order.

Here is a Python function that solves the problem:
```
def median_trapezium(a, b, c):
    sides = sorted([a, b, c])
    return sides[1]
```
This function sorts the three sides in ascending order and returns the middle value, which is the median length of the trapezium. For example, if the sides are 15, 25, and 35, the function will return 25, which is the median length.