
def get_lucid(n: int) -> list:
    result = []
    for i in range(2, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            continue
        j = 5
        while i % j != 0:
            j *= 5
        result.append(i)
    return result


