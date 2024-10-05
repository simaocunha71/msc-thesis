def closest_integer(value):
    value = float(value)
    return int(round(value))

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))