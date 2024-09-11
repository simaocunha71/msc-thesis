def perfect_squares(start, end):
    res = []
    for i in range(start, end + 1):
        if i ** 0.5 == int(i ** 0.5):
            res.append(i)
    return res


assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]

"""
Explanation:
We start by initializing an empty list called res. We then iterate over the range from the start to end + 1. For each number i in this range, we check if the square root of i is an integer by comparing i ** 0.5 to int(i ** 0.5). If they are equal, then i is a perfect square and we append it to the res list. Finally, we return the res list.
"""


def perfect_squares2(start, end):
    res = []
    for i in range(start, end + 1):
        if i ** 0.5 == int(i ** 0.5):
            res.append(i)
    return res


assert perfect_squares2(1, 30) == [1, 4, 9, 16, 25]


"""
Explanation:
The function perfect_squares2 is a slightly different version of perfect_squares. It also initializes an empty list called res and iterates over the range from the start to end + 1. For each number i in this range, it checks if the square root of i is an integer by comparing i ** 0.5 to int(i ** 0.5). If they are equal, then i is a perfect square and it appends it to the res list. Finally, it returns the res list.
"""


def perfect_squares3(start, end):
    res = []
    for i in range(start, end + 1):
        if i ** 0.5 == int(i ** 0.5):
            res.append(i)
    return res


assert perfect_squares3(1, 30) == [1, 4, 9,