def merge(lists: list) -> list:
    return [list(x) for x in zip(*lists)]