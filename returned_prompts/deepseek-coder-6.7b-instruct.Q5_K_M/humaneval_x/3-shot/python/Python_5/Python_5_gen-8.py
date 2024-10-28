    result = []
    for i in numbers:
        result.append(i)
        result.append(delimeter)
    if result:
        result.pop()  # remove last delimeter
    return result


