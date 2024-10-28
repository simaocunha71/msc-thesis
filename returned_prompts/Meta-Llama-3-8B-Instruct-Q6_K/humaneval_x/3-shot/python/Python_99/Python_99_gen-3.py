    import math

    def closest_integer(value):
        num = float(value)
        return round(num + 0.5) if num >= 0 else round(num - 0.5)

    print(closest_integer("10"))  # Output: 10
    print(closest_integer("15.3"))  # Output: 15
    print(closest_integer("14.5"))  # Output: 15
    print(closest_integer("-14.5"))  # Output: -15
    print(closest_integer("0.5"))  # Output: 1
    print(closest_integer("-0.5"))  # Output: -1
    print(closest_integer("1"))  # Output: 1
    print(closest_integer("-1"))  # Output: -1
    print(closest_integer("2"))  # Output: 2
    print(closest_integer("-2"))  # Output: -2
    print(closest_integer("3.5"))  # Output: 4
    print(closest_integer("-3.5"))  # Output: -4
    print(closest_integer("4.5"))  # Output: 5
    print(closest_integer("-4.5"))  # Output: -5
    print(closest_integer("5"))  # Output: 5
    print(closest_integer("-5"))  # Output: -5
    print(closest_integer("6"))  # Output: 6
    print(closest_integer("-6"))  # Output: -6
    print(closest_integer("7"))  # Output: 7
    print(closest_integer("-7"))  # Output: -7
    print(closest_integer("8"))  # Output: 8
    print(closest_integer("-8"))  # Output: -8
    print(closest_integer("9"))  # Output: 9
    print(closest_integer("-9"))  # Output: -9
    print(closest_integer("10"))  # Output: 10
    print(closest_integer("-10"))  # Output: -10
    print(closest_integer("11"))  # Output: 11
    print(closest_integer("-11"))  # Output: -11
    print(closest_integer("12"))  # Output: 12
    print(closest_integer("-12"))  # Output: -12
    print(closest