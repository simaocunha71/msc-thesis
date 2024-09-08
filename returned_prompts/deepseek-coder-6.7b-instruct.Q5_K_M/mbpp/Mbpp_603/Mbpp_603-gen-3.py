
def get_ludic(n):
    ludic_nums = []
    for i in range(1, n+1):
        if i % 2 != 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1)):
            ludic_nums.append(i)
    return ludic_nums

assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

"""

