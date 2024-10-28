def triplesSumToZero(l):
    """Return True if there are three distinct elements in the list that sum to zero, and False otherwise."""
    if len(l) < 3:
        return False
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

print(triplesSumToZero([1, 3, 5, 0]))
print(triplesSumToZero([1, 3, -2, 1]))
print(triplesSumToZero([1, 2, 3, 7]))
print(triplesSumToZero([2, 4, -5, 3, 9, 7]))
print(triplesSumToZero([1]))
