def max_run_uppercase(s):
    count = max_count = 0
    for char in s:
        if char.isupper():
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

print(max_run_uppercase('GeMKSForGERksISBESt'))
<jupyter_output>
5
<jupyter_text>
Q2. Write a Python program to check if a string is a pangram. A pangram is a sentence that contains all the letters of the alphabet at least once (case is irrelevant).
<jupyter_code>
