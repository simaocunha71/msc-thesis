The problem is asking to find the median length of a trapezium. A trapezium is a quadrilateral with two pairs of opposite sides, one pair being parallel. The median length is the length of the line segment from the mid-point of the top side to the bottom side.

However, the problem does not provide the lengths of the median and the distance between the mid-point of the top side and the bottom side. But we can assume that the median length is the length of the median, which is the average of the lengths of the top and bottom sides.

The unit test `assert median_trapezium(15,25,35)==20` suggests that the median length is the average of the lengths of the top and bottom sides.

Here is the solution:
```
def median_trapezium(a, b, c):
    return (a+b)/2
```
This function takes three arguments `a`, `b`, and `c`, which are the lengths of the top and bottom sides of the trapezium. It returns the median length, which is the average of the lengths of the top and bottom sides. The unit test `assert median_trapezium(15,25,35)==20` passes with this solution.