
def make_a_pile(n):
    result = []
    while n > 0:
        result.append(n)
        n = next_level(n)
    return result

def next_level(n):
    if n % 2 == 0:
        return n + 1
    else:
        return n + 2
