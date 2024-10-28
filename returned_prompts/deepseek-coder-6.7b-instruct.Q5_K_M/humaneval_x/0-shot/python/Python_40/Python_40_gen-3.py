
    l.sort()
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        left = i + 1
        right = len(l) - 1
        while left < right:
            current_sum = l[i] + l[left] + l[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()


The function works by sorting the input list and then iterating over it. For each element, it then uses two pointers to find a pair of numbers that sum to the negation of the current element.

If it finds such a pair, it returns True. If it goes through all the elements without finding such a triplet, it returns False. The use of the two pointers technique ensures that the function runs in O(n^2) time, where n is the length of the list.

The doctest module is used to test the function with the provided examples.
"""


def triples_sum_to_zero(l: list):
    l.sort()
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        left = i + 1
        right = len(l) - 1
        while left < right:
            current_sum = l[i] + l[left] + l[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                return True
    return False


print(triples_sum_to_zero([1, 3, 5, 0]))  # False
print(triples_sum_to_zero([1, 3, -2, 1]))  # True
print(triples_sum_to_zero([1, 2, 3, 7])) 