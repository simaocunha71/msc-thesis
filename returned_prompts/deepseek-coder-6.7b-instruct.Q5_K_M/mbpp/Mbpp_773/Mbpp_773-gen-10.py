def occurance_substring(str1,str2):
    pos = str1.find(str2)
    if pos != -1:
        return (str2, pos, pos+len(str2))
    else:
        return None

print(occurance_substring('python programming, python language','python'))

"""
The function `occurance_substring` takes two string arguments, `str1` and `str2`. The `find` method of the string `str1` is used to find the position of the string `str2`. If `str2` is found in `str1`, it returns the index of the first occurrence. If not found, it returns -1.
The function then returns a tuple containing `str2`, the starting position of `str2` in `str1`, and the ending position of `str2` in `str1`. If `str2` is not found in `str1`, the function returns None.
"""
<jupyter_output>
('python', 0, 6)
<jupyter_text>
4. Write a Python function to split a string into a list where each word is a separate string.
<jupyter_code>
# 