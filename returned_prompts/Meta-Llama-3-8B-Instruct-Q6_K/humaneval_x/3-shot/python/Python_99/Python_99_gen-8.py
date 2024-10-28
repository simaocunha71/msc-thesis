    import math

    def closest_integer(value):
        return round(float(value))

    # Alternative solution using math.ceil and math.floor
    # def closest_integer(value):
    #     return math.ceil(float(value)) if float(value) >= 0 else math.floor(float(value))  # Use math.ceil for positive numbers and math.floor for negative numbers. If the number is 0, it will be rounded to 0.
    #     # If the number is equidistant from two integers, round away from zero.
    #     # For example, closest_integer("14.5") should return 15 and closest_integer("-14.5") should return -15.