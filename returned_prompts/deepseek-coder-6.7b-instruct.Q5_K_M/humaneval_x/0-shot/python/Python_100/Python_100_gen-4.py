
    result = []
    stones = n
    for i in range(n):
        result.append(stones)
        if stones % 2 == 0:
            stones += 2
        else:
            stones += 2
    return result

print(make_a_pile(3))
print(make_a_pile(4))
print(make_a_pile(5))
print(make_a_pile(6))
print(make_a_pile(7))

Output:
[3, 5, 7]
[4, 6, 8, 10]
[5, 7, 9, 11, 13]
[6, 8, 10, 12, 14, 16]
[7, 9, 11, 13, 15, 17, 19]

Explanation:

The problem asks us to create a list where the number of stones at each index i represents the number of stones at level (i+1).

If the number of stones at the current level is even, we add 2 to get to the next level. If it's odd, we also add 2.

We repeat this process for n levels.

This is done by starting with n stones at the first level, then adding 2 more stones if the current level has an even number of stones, or 3 if it's odd.

We keep adding these stones to a list, which we return at the end.
"""

# 2.
"""
