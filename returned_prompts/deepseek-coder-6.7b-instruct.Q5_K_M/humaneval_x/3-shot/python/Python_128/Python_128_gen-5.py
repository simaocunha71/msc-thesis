    if not arr:
        return None
    sign = 1
    magnitude = 0
    for num in arr:
        if num < 0:
            sign *= -1
            magnitude += abs(num)
        elif num > 0:
            magnitude += num
    return sign * magnitude

