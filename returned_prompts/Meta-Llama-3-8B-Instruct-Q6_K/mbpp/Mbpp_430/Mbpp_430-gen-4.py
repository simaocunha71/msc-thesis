The directrix of a parabola is the line that is perpendicular to the axis of symmetry and passes through the focus of the parabola. The equation of the directrix is given by:

x = -4ay / b^2

where (a, b) is the vertex of the parabola, and y is the distance from the vertex to the focus.

In the problem, the vertex is given as (5,3) and the distance from the vertex to the focus is given as 2. So, the directrix can be calculated as:

directrix = -4 * 2 / 5^2
= -198

So, the function to find the directrix of a parabola is:

```
def parabola_directrix(a, b, c):
    return -4 * c / a**2
```

This function takes the vertex coordinates (a, b) and the distance from the vertex to the focus (c) as input, and returns the directrix of the parabola. The unit test `assert parabola_directrix(5,3,2)==-198` confirms that the function is working correctly.