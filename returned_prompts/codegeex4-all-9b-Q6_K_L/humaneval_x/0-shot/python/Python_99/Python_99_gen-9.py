def closest_integer(value):
    value = float(value)
    if value >= 0:
        return int(value + 0.5)
    else:
        return int(value - 0.5)

# Test cases
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15