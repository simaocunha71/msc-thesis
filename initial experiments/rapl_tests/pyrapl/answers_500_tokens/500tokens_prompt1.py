
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even = []
    while a < b:
        if a % 2 == 0:
            even.append(a)
        a += 1
    return even

def additions_between_integers(a, b):
    """Return addition and subtraction between each pair of integers in a and b."""
    addition = []
    for i in range(0, len(generate_integers(a, b)), 2):
        # Addition.
        if (i != len(generate_integers(a, b))) or (not generate_integers(a + i[1], i[1] - 1) in [x for x in addition]):
            addition.append((addition + a)[0] + (i[0] + i[1]) % modul)
    # Subtraction.
    subtractions = []
    for j in range(2, len(generate_integers(a, b)), 2):
        if not generate_integers(j - a, j + a)[0] in [x for x in addition] or (not generate_integers(j, a) in [x for x in subtractions]):
            subtractions.append((generate_integers(a, j)[0] - a) % modul)
    # Sort by ascending order of the positive additions and subtractions between each pair of integers from a and b.
    addition = list(sorted(addition))
    subtraction = list(sorted(subtractions))
    return [a] + addition + subtraction
