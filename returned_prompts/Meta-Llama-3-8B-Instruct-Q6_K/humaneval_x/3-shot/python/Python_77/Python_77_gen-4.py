    import math
    return math.isclose(a, round(a ** (1.0 / 3))) or math.isclose(a, -round(-a ** (1.0 / 3)))  # or a == 0


