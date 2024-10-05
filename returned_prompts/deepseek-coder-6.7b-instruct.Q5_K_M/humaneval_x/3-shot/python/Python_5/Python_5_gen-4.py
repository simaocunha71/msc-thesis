    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    if result:
        result.pop()  # Remove last delimeter
    return result


