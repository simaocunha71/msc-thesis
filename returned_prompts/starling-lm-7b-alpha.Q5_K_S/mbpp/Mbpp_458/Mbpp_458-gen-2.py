def rectangle_area(length, width):
    """
    Find the area of a rectangle.

    Parameters
    ----------
    length : int
        The length of the rectangle.
    width : int
        The width of the rectangle.

    Returns
    -------
    int
        The area of the rectangle.
    """
    return length * width


# Testing
assert rectangle_area(10, 20) == 200

```
Here's one way to define and test a function to calculate the area of a rectangle, given the length and width as parameters. The function `rectangle_area` multiplies the length and width together to find the area, and then returns the result as an integer. The provided `assert` statement tests whether the function returns the correct result when given a length of 10 and a width of 20, which should be 200.

To use this function, you can simply call it with the desired length and width as arguments. For example, `rectangle_area(5, 10)` would return 50, as the area of a rectangle with a length of 5 and a width of 10 is 50.

It's important to note that the function assumes both the length and width are positive integers. If you need to handle non-integer values or negative values, you may need to add additional logic to the function.
```
```