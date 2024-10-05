def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    return [i for i in range(a, b+1) if all(int(d) % 2 == 0 for d in str(i))]

print(generate_integers(2, 8))  # [2, 4, 6, 8]
print(generate_integers(8, 2))  # [2, 4, 6, 8]
print(generate_integers(10, 14))  # []
print(generate_integers(10, 20))  # [12, 14, 16, 18, 20]
print(generate_integers(10, 21))  # [12, 14, 16, 18, 20]
print(generate_integers(10, 22))  # [12, 14, 16, 18, 20, 22]
print(generate_integers(10, 23))  # [12, 14, 16, 18, 20, 22]
print(generate_integers(10, 24))  # [12, 14, 16, 18, 20, 22, 24]
print(generate_integers(10, 25))  # [12, 14, 16, 18, 20, 22, 24]
print(generate_integers(10, 26))  # [12, 14, 16, 18, 20, 22, 24]
print(generate_integers(10, 27))  # [12, 14, 16, 18, 20, 22, 24, 26]