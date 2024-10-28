def combinations_colors(colors: list, n: int) -> list:
    result = []
    for i in range(0, len(colors) + 1):
        result.extend([tuple(colors[i:i+n]) for i in range(len(colors) - n + 1)])
    return result