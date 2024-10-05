    import math

    def is_right_angle(a, b, c):
        return math.isclose(a**2 + b**2, c**2)

    return is_right_angle(a, b, c) or is_right_angle(b, c, a) or is_right_angle(a, c, b)

    # return math.isclose(a**2 + b**2, c**2) or math.isclose(b**2 + c**2, a**2) or math.isclose(a**2 + c**2, b**2)