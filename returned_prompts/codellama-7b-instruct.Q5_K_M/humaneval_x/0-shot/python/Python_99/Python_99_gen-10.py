
def closest_integer(value):
    x = float(value)
    return int(x + abs(x) / 2)
