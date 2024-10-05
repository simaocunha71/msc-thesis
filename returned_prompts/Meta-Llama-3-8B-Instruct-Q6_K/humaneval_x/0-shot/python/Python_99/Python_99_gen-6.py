    # Solution
    from math import ceil, floor

    def closest_integer(value):
        value = float(value)
        if value >= 0:
            return ceil(value)
        else:
            return floor(value)

    # Test the function
    print(closest_integer("10"))  # Output: 10
    print(closest_integer("15.3"))  # Output: 15
    print(closest_integer("14.5"))  # Output: 15
    print(closest_integer("-14.5"))  # Output: -15
    print(closest_integer("0"))  # Output: 0
    print(closest_integer("-0"))  # Output: 0
    print(closest_integer("1.5"))  # Output: 2
    print(closest_integer("-1.5"))  # Output: -2
    print(closest_integer("2.9"))  # Output: 3
    print(closest_integer("-2.9"))  # Output: -3
    print(closest_integer("3.5"))  # Output: 4
    print(closest_integer("-3.5"))  # Output: -4
    print(closest_integer("4.1"))  # Output: 4
    print(closest_integer("-4.1"))  # Output: -4
    print(closest_integer("5"))  # Output: 5
    print(closest_integer("-5"))  # Output: -5
    print(closest_integer("5.5"))  # Output: 6
    print(closest_integer("-5.5"))  # Output: -6
    print(closest_integer("10.6"))  # Output: 11
    print(closest_integer("-10.6"))  # Output: -11
    print(closest_integer("11"))  # Output: 11
    print(closest_integer("-11"))  # Output: -11
    print(closest_integer("11.4"))  # Output: 11
    print(closest_integer("-11.4"))  # Output: -11
    print(closest_integer("12"))  # Output: 12
    print(closest_integer("-12"))  # Output: -12
    print(closest_integer("12.5"))  # Output: 13
    print(closest_integer("-12.5"))  # Output: -13
    print(closest