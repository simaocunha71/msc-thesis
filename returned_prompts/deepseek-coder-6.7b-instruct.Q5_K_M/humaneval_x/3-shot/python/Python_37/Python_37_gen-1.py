    evens = sorted([l[i] for i in range(0, len(l), 2)])
    result = [evens.pop(0) if i % 2 == 0 else l[i] for i in range(len(l))]
    return result


