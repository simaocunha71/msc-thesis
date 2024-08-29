def max_run_uppercase(s):
    count = 0
    max_count = 0
    for i in s:
        if i.isupper():
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

print(max_run_uppercase('GeMKSForGERksISBESt'))

# Explanation:
# The function iterates over the characters in the string. It checks if the character is an uppercase letter. If it is, it increments a counter. If the counter is greater than the max_count, it updates max_count with the current value of counter. If the character is not uppercase, it resets the counter to 0. At the end of the iteration, it returns the maximum count of uppercase letters found in the string.
<jupyter_output>
5
<jupyter_text>
Question 2:
<jupyter_code>
