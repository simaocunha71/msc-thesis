
def check_occurences(lst: list) -> dict:
    return {tuple(sorted(x)): lst.count(x) for x in lst}


