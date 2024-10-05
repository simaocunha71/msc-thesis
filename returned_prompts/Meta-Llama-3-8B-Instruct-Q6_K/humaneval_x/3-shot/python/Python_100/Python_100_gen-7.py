    result = [n]
    n += 1
    while n <= 1000:  # Assuming the number of levels will not exceed 1000
        if n % 2 == 1:
            result.append(n)
            n += 1
        else:
            result.append(n)
            n += 2

    return result


