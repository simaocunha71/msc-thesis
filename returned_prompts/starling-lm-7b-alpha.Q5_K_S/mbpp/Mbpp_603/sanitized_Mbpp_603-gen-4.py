def get_ludic(num):
    """
    Get all lucid numbers smaller than or equal to a given integer.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    res = []
    for i in range(1, num + 1):
        if all(i % j == 0 for j in range(2, int(i ** 0.5) + 1)):
            res.append(i)
    return res