def combinations_colors(colors,n):
    result = []
    for i in range(len(colors)):
        result.append(tuple(colors[i] for _ in range(n)))
    return result