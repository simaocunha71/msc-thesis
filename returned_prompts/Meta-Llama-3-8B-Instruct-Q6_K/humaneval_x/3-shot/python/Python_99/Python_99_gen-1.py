    from math import floor, ceil

    def closest_integer(value):
        num = float(value)
        if num - int(num) < 0.5:
            return floor(num)
        else:
            return ceil(num)

# Test your function
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15
print(closest_integer("17.8"))  # Output: 18
print(closest_integer("-17.8"))  # Output: -18
print(closest_integer("0"))  # Output: 0
print(closest_integer("-0"))  # Output: -0
print(closest_integer("0.5"))  # Output: 1
print(closest_integer("-0.5"))  # Output: -1
print(closest_integer("1.5"))  # Output: 2
print(closest_integer("-1.5"))  # Output: -2
print(closest_integer("2.5"))  # Output: 3
print(closest_integer("-2.5"))  # Output: -3
print(closest_integer("3.5"))  # Output: 4
print(closest_integer("-3.5"))  # Output: -4
print(closest_integer("4.5"))  # Output: 5
print(closest_integer("-4.5"))  # Output: -5
print(closest_integer("5.5"))  # Output: 6
print(closest_integer("-5.5"))  # Output: -6
print(closest_integer("6.5"))  # Output: 7
print(closest_integer("-6.5"))  # Output: -7
print(closest_integer("7.5"))  # Output: 8
print(closest_integer("-7.5"))  # Output: -8
print(closest_integer("8.5"))  # Output: 9
print(closest_integer("-8.5"))  # Output: -9
print(closest_integer("9.5"))  # Output: 10
print(closest_integer("-9.5"))  # Output: -10
print(closest_integer("10.5"))  # Output: 11
print(closest