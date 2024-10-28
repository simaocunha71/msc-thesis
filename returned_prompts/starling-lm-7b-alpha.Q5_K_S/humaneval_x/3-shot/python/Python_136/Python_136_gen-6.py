    negative = None
    positive = None

    for i in lst:
        if i < 0 and (negative is None or i > negative):
            negative = i
        elif i > 0 and (positive is None or i < positive):
            positive = i

    return negative, positive


