closest_integer = lambda value: int(round(float(value)))




def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # Convert the value to a float
    float_value = float(value)

    # Round the float to the closest integer
    closest_int = round(float_value)

    # Return the closest integer
    return closest_int




# Test the function
print(closest_integer("10"))  # Should print: 10
print(closest_integer("15.3"))  # Should print: 15
print(closest_integer("14.5"))  # Should print: 15
print(closest_integer("-14.5"))  # Should print: -15




```

```python
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest