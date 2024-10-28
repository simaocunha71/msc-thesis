
def eat(number, need, remaining):
    if number >= need:
        return [number, remaining]
    else:
        return [number + remaining, 0]