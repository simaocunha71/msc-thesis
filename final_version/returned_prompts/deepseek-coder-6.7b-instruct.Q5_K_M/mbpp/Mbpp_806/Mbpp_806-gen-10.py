def max_run_uppercase(s):
    max_count = 0
    count = 0
    for i in s:
        if i.isupper():
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

print(max_run_uppercase('GeMKSForGERksISBESt'))  # 5

"""
The function works by iterating over each character in the string. If the character is uppercase, it increases the count and updates max_count with the new count if count is greater than max_count. If the character is not uppercase, it resets the count to 0. At the end, it returns the maximum count, which is the maximum run of uppercase characters.
"""
<jupyter_output>
5
<jupyter_text>
6. Write a Python function to find the minimum run of lowercase characters in the given string.
<jupyter_code>
