    result = []

    for row in range(len(lst)):
        for col in range(len(lst[row])):
            if lst[row][col] == x:
                result.append((row, col))

    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)

    return result

