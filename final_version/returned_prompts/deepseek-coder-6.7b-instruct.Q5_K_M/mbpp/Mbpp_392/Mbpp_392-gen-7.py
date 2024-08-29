
def get_max_sum(n):
    if n == 0:
        return 0
    else:
        return max((get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5)), n)

assert get_max_sum(60) == 106
"""

The function `get_max_sum(n)` returns the maximum possible sum that can be obtained by cutting up the rod of length `n` and selling the pieces. This is done by recursively calling the function on the values `n//2`, `n//3`, `n//4`, and `n//5`, and taking the maximum of the result and `n`.

If `n` is 0, the function returns 0, as there is no rod left to cut.

The `assert` statement at the end checks that the function is working correctly. It should return 106 if the function is