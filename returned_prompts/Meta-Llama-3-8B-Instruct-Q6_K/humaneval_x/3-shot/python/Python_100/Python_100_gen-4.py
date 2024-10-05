    result = [n]
    i = 1
    while n > 1:
        n -= 1
        if n % 2 == 0:
            n += 1
        result.append(n)
        n -= 1
    return result[::-1]  # reverse the list because we appended in reverse order


