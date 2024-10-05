    import math

    def euclid_distance(a, b, c):
        return math.sqrt(a ** 2 + b ** 2)

    if euclid_distance(b, c, a) == a and euclid_distance(a, c, b) == b and euclid_distance(a, b, c) == c:
        return True
    return False


