def max_run_uppercase(s):
    count, max_count = 0, 0
    for char in s:
        if char.isupper():
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    return max_count

print(max_run_uppercase('GeMKSForGERksISBESt'))  # 5

Explanation:
The function works by iterating over each character in the string. If the character is uppercase, it increments the count variable and updates max_count with the maximum of count and max_count so far. If the character is not uppercase, it resets the count variable to 0. At the end, the function returns max_count which holds the length of the longest run of uppercase characters.
"""

