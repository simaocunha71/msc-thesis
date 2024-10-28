
    l.sort()
    for i in range(len(l)-2):
        if i > 0 and l[i] == l[i-1]:
            continue
        start = i + 1
        end = len(l) - 1
        while start < end:
            sum = l[i] + l[start] + l[end]
            if sum < 0:
                start += 1
            elif sum > 0:
                end -= 1
            else:
                return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()


Explanation:

The function first sorts the input list. Then it iterates over the list with three nested loops:

1. The outer loop selects the current number `l[i]`.

2. The inner loop is a two-pointer technique where `start` and `end` are pointers to the beginning and end of the remaining list. The sum of `l[i]`, `l[start]`, and `l[end]` is checked. If the sum is less than zero, the `start` pointer is increased, and if the sum is greater than zero, the `end` pointer is decreased.

3. If the sum is equal to zero, the function returns True.

4. If the inner loop finishes without finding a sum of zero, the outer loop continues with the next number.

5. If the outer loop finishes without finding three numbers that sum to zero, the function returns False.
"""


def triples_sum_to_zero(l: list) -> bool:
    l.sort()
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        start = i + 1
        end = len(l) - 1
        while start < end:
            sum = l[i] + l[start] + l[end]
            if sum < 0:
                start += 1
            elif sum > 0:
                end -= 1
            else:
                return True
    return False


if __name__ == "__