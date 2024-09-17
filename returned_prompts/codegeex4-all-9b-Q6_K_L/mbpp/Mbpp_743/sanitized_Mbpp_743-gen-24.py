def rotate_right(lst: list, num: int) -> list:
    return lst[-num:] + lst[:-num]