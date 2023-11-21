
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    result = []
    while a < b:
        if (a % 2) == (b % 2):
            result.append(a)
        else:
            break
        a += 1

    return sorted(result)

def generate_integers_evenly(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b in such a way that they will be evenly distributed.

    For example:
    generate_integers_evenly(2, 8) => [4]
    generate_integers_evenly(10, 14) => []
    """

    result = list(generate_integers(a, b))
    even_result = filter(lambda x: (x % 2), result)
    return sorted(even_result)