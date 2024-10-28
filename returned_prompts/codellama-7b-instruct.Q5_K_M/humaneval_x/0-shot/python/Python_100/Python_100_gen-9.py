
def make_a_pile(n):
    result = []
    for i in range(n):
        result.append(n)
        if n % 2 == 0:
            n += 1
        else:
            n += 2
    return result
