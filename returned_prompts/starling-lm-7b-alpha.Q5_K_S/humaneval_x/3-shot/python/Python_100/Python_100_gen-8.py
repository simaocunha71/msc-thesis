    result = []
    curr = n
    while curr > 0:
        result.append(curr)
        if curr % 2 == 0:
            curr += 2
        else:
            curr += 1
    return result


