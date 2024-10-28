    result = []
    minimum = min(lst)
    maximum = max(lst)
    while maximum in lst:
        result.append(maximum)
        lst.remove(maximum)
    while minimum in lst:
        result.append(minimum)
        lst.remove(minimum)
    return result


