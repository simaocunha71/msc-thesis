def max_run_uppercase(s):
    count = max_count = 0
    for ch in s:
        if ch.isupper():
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

print(max_run_uppercase('GeMKSForGERksISBESt'))

# OUTPUT: 5

# Explanation: In the given string 'GeMKSForGERksISBESt', maximum run of uppercase characters is 5.
<jupyter_output>
5
<jupyter_text>
