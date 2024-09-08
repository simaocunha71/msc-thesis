def next_Perfect_Square(num):
    import math
    if num < 0:
        return None
    root = math.ceil(math.sqrt(num))
    return root * root