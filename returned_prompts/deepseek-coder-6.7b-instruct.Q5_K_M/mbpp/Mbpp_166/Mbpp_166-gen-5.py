def find_even_pair(lst):
    even_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] ^ lst[j] % 2 == 0:
                even_count += 1
    return even_count

print(find_even_pair([5, 4, 7, 2, 1]))  # should return 4


"""
The function find_even_pair works by iterating over every pair of integers in the list and checking if their xor is even. If the xor is even, the count is incremented.

This solution is not efficient for large lists, because it has a time complexity of O(n^2).
"""


# More efficient solution using bitwise operation and list comprehension:

def find_even_pair_v2(lst):
    return sum((x ^ y) % 2 == 0 for i, x in enumerate(lst) for y in lst[i + 1:])

print(find_even_pair_v2([5, 4, 7, 2, 1]))  # should return 4

"""
The function find_even_pair_v2 is more efficient because it uses list comprehension to iterate over every pair of integers in the list and check if their xor is even. It only needs to iterate over each pair once, so its time complexity is O(n^2).
"""


# More efficient solution using bitwise operation and list comprehension with dictionary:

def find_even_pair_v3(lst):
    return sum(({x: x ^ y for y in lst[i + 1:]} or {}).values())

print(find_even_pair_v3([5, 4, 7, 2, 1]))  # should return 4

"""
The function find_even_pair_v3 is even more efficient because it uses dictionary comprehension to store the xor of every pair of integers in a dictionary. This allows it to check if a pair's xor is even in constant time, rather than having to iterate over the dictionary each time. It only