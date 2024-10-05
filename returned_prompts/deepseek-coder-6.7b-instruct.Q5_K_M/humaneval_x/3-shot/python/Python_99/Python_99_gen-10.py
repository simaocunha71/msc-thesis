    import math
    value = float(value)
    return math.floor(value) if abs(value - math.floor(value)) < abs(value - math.ceil(value)) else math.ceil(value)


