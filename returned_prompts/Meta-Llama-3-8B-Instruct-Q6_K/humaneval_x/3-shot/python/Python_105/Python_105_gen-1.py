    names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = []
    for num in sorted([x for x in arr if 1 <= x <= 9]):
        result.append(names[num])
    result.reverse()
    return result


