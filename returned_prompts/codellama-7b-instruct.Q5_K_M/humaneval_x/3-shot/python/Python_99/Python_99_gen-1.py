    value = float(value)
    if value % 1 == 0.5:
        if value < 0:
            return int(value - 0.5)
        else:
            return int(value + 0.5)
    else:
        return int(value)
