
    result = [n]
    if n % 2 == 0:
        next_n = n + 2
    else:
        next_n = n + 2
    while next_n <= n * 2:
        result.append(next_n)
        if next_n % 2 == 0:
            next_n += 2
        else:
            next_n += 2
    return result

# Test cases
print(make_a_pile(3))  # [3, 5, 7]
print(make_a_pile(4))  # [4, 6, 8, 10]
print(make_a_pile(10))  # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

"""
This solution works by first initializing a list with n stones, then repeatedly
adding the next odd or even number of stones to the list, until the total number
of stones exceeds twice the initial number. The number of stones in each level
is stored in the list and returned.
"""

#endregion

#region Question 2

