    def helper(num, a, b, c):
        if num >= 10:
            return helper(num-10, b, c, a) + b
        elif num >= 9:
            return helper(num-9, b, c, a) + c
        elif num >= 5:
            return helper(num-5, a, c, b) + a
        else:
            return helper(num-4, c, b, a) + c

    if number > 1000:
        raise ValueError("Number must be less than or equal to 1000")
    if number == 0:
        return ""
    return helper(number, "M", "M", "M")


