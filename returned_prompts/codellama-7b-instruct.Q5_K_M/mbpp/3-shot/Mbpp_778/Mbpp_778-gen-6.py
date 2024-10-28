
def pack_consecutive_duplicates(lst: list) -> list:
    return [list(g) for k, g in groupby(lst)]


