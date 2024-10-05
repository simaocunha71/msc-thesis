    value = float(value)
    if value > 0:
        return int(value) + 1 if value - int(value) >= 0.5 else int(value)
    else:
        return int(value) - 1 if int(value) - value >= 0.5 else int(value)

