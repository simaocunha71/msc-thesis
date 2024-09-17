```
def median_trapezium(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[1]
```


The problem is asking to write a function that finds the median length of a trapezium. A trapezium has three sides, and the median is the middle value when the sides are sorted in ascending order.

The unit test `assert median_trapezium(15,25,35)==20` suggests that the function should return the middle value of the three sides, which is 20 in this case.

The function takes three parameters, the lengths of the three sides of the trapezium, sorts them in ascending order, and returns the middle value.

Here is the solution in Python:
```
def median_trapezium(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[1]
```


This function works by first creating a list of the three sides, then sorting this list in ascending order. The median is the middle value of this sorted list, which is accessed using the index 1 (since list indices start at 0). The function then returns this median value.