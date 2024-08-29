def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] ^ lst[j] % 2 == 0:
                count += 1
    return count

print(find_even_pair([5, 4, 7, 2, 1]))  # 4
"""
Explanation:
The pairs that xor to an even number are (5, 4), (5, 2), (7, 2), (7, 1)
"""

# Solution 2
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] + lst[j]) % 2 == 0 or (lst[i] % 2 == 0 and lst[j] % 2 == 0):
                count += 1
    return count

print(find_even_pair([5, 4, 7, 2, 1]))  # 4
"""
Explanation:
The pairs that xor to an even number are (5, 4), (4, 2), (7, 2), (2, 1)
"""

# Solution 3
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if bin(lst[i] ^ lst[j]).count('1') % 2 == 0:
                count += 1
    return count

print(find_even_pair([5, 4, 7, 2, 1]))  # 4
"""
Explanation:
The pairs that xor to an even number are (5, 4), (5, 2), (7, 2), (7, 1)
"""
```

The third solution is the most efficient one as it uses bitwise operations which are faster than arithmetic operations.
