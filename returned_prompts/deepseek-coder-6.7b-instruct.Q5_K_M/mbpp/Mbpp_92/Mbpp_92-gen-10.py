def is_undulating(n):
    s = str(n)
    prev = None
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] or (prev is not None and prev == s[i]):
            return False
        prev = s[i]
    return True

print(is_undulating(1212121))  # True

"""
Explanation:

The function works by converting the number to a string and iterating over it. For each character in the string, it checks if the next character is the same. If it is, the function returns False because the number is not undulating.

If the next character is different, the function checks if the previous character is the same. If it is, the function returns False because the number is not undulating.

If the function manages to iterate over the entire string without returning False, it means the number is undulating and the function returns True.
"""

# Problem 2

