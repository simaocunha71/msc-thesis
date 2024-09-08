
def find_even_pair(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] ^ arr[j] % 2 == 0:
                count += 1
    return count

assert find_even_pair([5, 4, 7, 2, 1]) == 4
assert find_even_pair([3, 2, 1]) == 1
assert find_even_pair([1]) == 0
assert find_even_pair([]) == 0
"""

def find_even_pair(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] ^ arr[j]) % 2 == 0:
                count += 1
    return count

assert find_even_pair([5, 4, 7, 2, 1]) == 4
assert find_even_pair([3, 2, 1]) == 1
assert find_even_pair([1]) == 0
assert find_even_pair([]) == 0
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
"""
