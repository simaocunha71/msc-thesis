def larg_nnum(lst: list, n: int) -> list:
    lst.sort(reverse=True)
    return lst[:n]