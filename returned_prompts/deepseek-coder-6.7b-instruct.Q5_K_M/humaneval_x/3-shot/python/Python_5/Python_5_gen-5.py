    result = []

    for n in numbers:
        result.append(n)
        result.append(delimeter)

    if result:
        result.pop()  # remove the last delimeter

    return result


