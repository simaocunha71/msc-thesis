
def eat(number, need, remaining):
    total = number + need
    if total > remaining:
        return [remaining + number, 0]
    else:
        return [remaining + number, remaining - total]
