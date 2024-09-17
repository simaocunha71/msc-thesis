def get_ludic(num: int) -> list:
    ludics = [2]
    for i in range(3, num + 1):
        if all(i % f != 0 for f in ludics):
            ludics.append(i)
    return ludics