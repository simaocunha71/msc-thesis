    from math import floor, ceil

    if value.startswith('-'):
        value = value[1:]
        return -ceil(float(value)) if float(value) % 1 >= 0.5 else -floor(float(value))
    else:
        return ceil(float(value)) if float(value) % 1 >= 0.5 else floor(float(value))



