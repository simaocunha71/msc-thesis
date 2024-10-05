    result = []
    for num in x:
        if not any(i % 2 == 0 for i in str(num)):
            result.append(num)

    return sorted(result)


