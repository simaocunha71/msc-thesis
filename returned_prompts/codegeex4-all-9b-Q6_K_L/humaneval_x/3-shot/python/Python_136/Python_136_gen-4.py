    positive = []
    negative = []
    for num in lst:
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
    if not positive:
        positive = None
    else:
        positive = max(positive)
    if not negative:
        negative = None
    else:
        negative = min(negative)
    return (negative, positive)

