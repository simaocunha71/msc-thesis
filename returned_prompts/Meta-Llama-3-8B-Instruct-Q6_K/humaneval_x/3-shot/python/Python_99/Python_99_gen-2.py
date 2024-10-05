    import math

    def closest_integer(value):
        num = float(value)
        if num == int(num):
            return int(num)
        else:
            return round(num) if num > 0 else round(num, 0) if num < 0 else 0


