def max_run_uppercase(s):
    count = 0
    max_count = 0
    for ch in s:
        if ch.isupper():
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

print(max_run_uppercase('GeMKSForGERksISBESt'))  # Outputs: 5

Explanation:
The function iterates through each character in the string. If the character is uppercase, it increments the count and checks if the count is greater than the maximum count (initialized as 0). If true, it updates the maximum count. If the character is not uppercase, it resets the count back to 0. Finally, the function returns the maximum count of uppercase characters.
"""

