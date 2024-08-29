def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] ^ lst[j] % 2 == 0:
                count += 1
    return count

print(find_even_pair([5, 4, 7, 2, 1]))  # should return 4
"""
The function works by iterating over all pairs of integers in the list and checking whether the xor of the pair results in an even number. If the xor is even, it increments the count. The function returns the total count once it has checked all pairs.
"""

# Alternative Solution:
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] + lst[j]) % 2 == 0 or lst[i] == lst[j]:
                count += 1
    return count

print(find_even_pair([5, 4, 7, 2, 1]))  # should return 4
"""
This alternative solution also uses a similar approach to the first one, but instead of checking whether the xor of the pair results in an even number, it checks whether the sum of the pair or whether both numbers are the same (since xor of same numbers is 0) results in an even number. This is because an even number in binary form ends with 0, and the xor of two numbers ends with 0 if and only if both numbers end with 0.
"""

# Alternative Solution:
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if bin(lst[i] ^ lst[j]).count('0') % 2 == 0:
                count += 1
    return count

print(find_even_pair([5, 4, 7, 2, 1]))  # should return 4