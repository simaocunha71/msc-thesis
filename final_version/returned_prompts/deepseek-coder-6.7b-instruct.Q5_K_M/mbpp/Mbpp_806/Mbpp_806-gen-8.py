def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for c in s:
        if c.isupper():
            current_run += 1
        else:
            if current_run > max_run:
                max_run = current_run
            current_run = 0
    return max(max_run, current_run)

print(max_run_uppercase('GeMKSForGERksISBESt'))  # 5

"""
Explanation:

The function takes a string as input and initializes two variables - max_run and current_run - to 0. 
The max_run is the maximum run of uppercase characters encountered so far and current_run is the current run of uppercase characters. 

We then iterate over each character in the string. If the character is uppercase (c.isupper() is True), we increment current_run. 

If the character is not uppercase (c.isupper() is False), we check if the current run is greater than the max_run. 
If it is, we update max_run with the current run. After that, we reset the current_run to 0.

At the end of the loop, we return the maximum of max_run and current_run because the last run of uppercase characters might be the longest one.
"""
<jupyter_output>
5
<jupyter_text>
Problem 5:
<jupyter_code>
