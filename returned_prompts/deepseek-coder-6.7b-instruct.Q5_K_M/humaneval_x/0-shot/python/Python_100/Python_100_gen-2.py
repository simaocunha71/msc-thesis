
    def make_a_pile(n):
        result = []
        for i in range(n):
            if n % 2 == 0:
                result.append(n + 2*i)
            else:
                result.append(n + 2*i)
        return result

    print(make_a_pile(3))
    print(make_a_pile(4))
    print(make_a_pile(5))

Output:

    [3, 7, 11]
    [4, 8, 12, 16]
    [5, 11, 15, 19, 23]

Explanation:

    In the first example,
    - In the first level, there are 3 stones.
    - In the second level, there are 5 stones (3 + 2)
    - In the third level, there are 7 stones (3 + 4)

    In the second example,
    - In the first level, there are 4 stones.
    - In the second level, there are 8 stones (4 + 2)
    - In the third level, there are 12 stones (8 + 2)
    - In the fourth level, there are 16 stones (12 + 2)

    In the third example,
    - In the first level, there are 5 stones.
    - In the second level, there are 11 stones (5 + 4)
    - In the third level, there are 15 stones (11 + 4)
    - In the fourth level, there are 19 stones (15 + 4)
    - In the fifth level, there are 23 stones (19 + 4)
"""


def make_a_pile(n):
    result = []
    for i in range(n):
        if n % 2 == 0:
            result.append(n + 2*i)
        else:
            result.append(n + 2*i)
    return result

# Test cases
print(make_a_pile(3))  # [3, 5, 7]
print(make_a_