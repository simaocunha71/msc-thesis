    value = float(value)
    rounded_value = round(value)
    if abs(rounded_value) < abs(value):
        rounded_value = -rounded_value
    return rounded_value


