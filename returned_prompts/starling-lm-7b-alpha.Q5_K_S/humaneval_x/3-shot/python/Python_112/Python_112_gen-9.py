    result = ""
    for elem in s:
        if elem not in c:
            result += elem

    if result == result[::-1]:
        return (result, True)
    else:
        return (result, False)


