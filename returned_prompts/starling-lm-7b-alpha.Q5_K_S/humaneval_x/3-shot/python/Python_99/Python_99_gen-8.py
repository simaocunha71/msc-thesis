    value = float(value)
    if value == int(value):
        return int(value)
    elif value > 0:
        return int(value + 0.5)
    else:
        return int(value - 0.5)


