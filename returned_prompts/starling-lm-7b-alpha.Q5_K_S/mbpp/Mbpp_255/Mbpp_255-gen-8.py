
def combinations_colors(colors: list, length: int) -> list:
    combinations = []
    for i in range(len(colors)):
        combinations.append(colors[i])
    while True:
        if len(combinations) >= length:
            yield tuple(combinations[:length])
        else:
            if len(combinations) > 0:
                combinations.pop(-1)
            else:
                break


