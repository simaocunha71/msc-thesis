def find_first_occurrence(arr: list, x: int) -> int:
    if x in arr:
        return arr.index(x)
    else:
        return -1