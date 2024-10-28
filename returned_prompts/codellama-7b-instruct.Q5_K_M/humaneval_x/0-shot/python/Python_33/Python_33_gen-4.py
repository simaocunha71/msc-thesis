
def sort_third(l: list) -> list:
    return [l[i] for i in range(len(l)) if i % 3 != 0] + sorted(l[i] for i in range(len(l)) if i % 3 == 0)