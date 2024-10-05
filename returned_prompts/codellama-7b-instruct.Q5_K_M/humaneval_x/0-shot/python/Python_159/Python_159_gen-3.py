
def eat(number, need, remaining):
    total = number + remaining
    if total >= need:
        return [need, total - need]
    else:
        return [total, 0]
