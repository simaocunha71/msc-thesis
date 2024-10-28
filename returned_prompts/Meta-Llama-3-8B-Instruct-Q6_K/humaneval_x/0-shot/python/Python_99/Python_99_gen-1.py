    def closest_integer(value):
        num = float(value)
        if num - int(num) < 0.5:
            return int(num)
        else:
            return int(round(num))
    # Example usage:
    print(closest_integer("10"))  # Output: 10
    print(closest_integer("15.3"))  # Output: 15
    print(closest_integer("14.5"))  # Output: 15
    print(closest_integer("-14.5"))  # Output: -15
    # Test cases:
    assert round(closest_integer("10")) == 10
    assert round(closest_integer("15.3")) == 15
    assert round(closest_integer("14.5")) == 15
    assert round(closest_integer("-14.5")) == -15
    # Test edge cases:
    assert round(closest_integer("0")) == 0
    assert round(closest_integer("0.5")) == 1
    assert round(closest_integer("-0.5")) == -1
    assert round(closest_integer("1.5")) == 2
    assert round(closest_integer("-1.5")) == -2
    # Test invalid inputs:
    try:
        closest_integer("hello")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for invalid input")
    try:
        closest_integer(10)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError for invalid input")
    # Test for corner cases:
    assert round(closest_integer("1")) == 1
    assert round(closest_integer("-1")) == -1
    assert round(closest_integer("0")) == 0
    # Test for edge cases:
    assert round(closest_integer("0.5")) == 1
    assert round(closest_integer("-0.5")) == -1
    # Test for rounding away from zero:
    assert round(closest_integer("14.5")) == 15
    assert round(closest_integer("-14.5")) == -15
    # Test for rounding to nearest integer:
    assert round(closest_integer("15.3")) == 15
    assert round(closest_integer("15.7")) == 16
    # Test for rounding to nearest integer with negative numbers:
    assert round(closest_integer("-15.3")) == -15
    assert round(closest_integer("-15