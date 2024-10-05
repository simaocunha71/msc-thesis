    result = []
    if n > 0:
        for i in range(2, n):
            if i < n and i > 1:
                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        break
                else:
                    result.append(i)

    return result


