def closest_integer(value):
    value = float(value)
    if value >= 0:
        return int(value + 0.5)
    else:
        return int(value - 0.5)

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))