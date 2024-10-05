
def closest_integer(value):
    number = float(value)
    floor = int(number)
    ceil = int(number) + 1
    if number - floor == 0:
        return floor
    elif number - ceil == 0:
        return ceil
    else:
        return floor if number - floor > number - ceil else ceil
