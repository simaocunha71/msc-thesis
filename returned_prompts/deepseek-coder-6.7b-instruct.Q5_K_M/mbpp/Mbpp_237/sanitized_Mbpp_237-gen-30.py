def check_occurences(lst: list) -> dict:
    return {tuple(sorted(k)): lst.count(k) for k in lst}