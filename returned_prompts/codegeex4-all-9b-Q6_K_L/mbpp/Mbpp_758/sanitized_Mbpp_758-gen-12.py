def unique_sublists(lst: list) -> dict:
    return {tuple(sublist): sublist.count(tuple(sublist)) for sublist in lst}