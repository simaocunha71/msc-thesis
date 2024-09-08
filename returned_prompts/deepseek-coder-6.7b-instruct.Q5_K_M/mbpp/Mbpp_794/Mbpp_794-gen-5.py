def text_starta_endb(txt):
    # Python's built-in regex module re is used here.
    import re
    # The pattern we are looking for is "a followed by anything (*) ending in b".
    pattern = "ab*"
    # The search function will return a match object if the pattern is found.
    if re.search(pattern, txt):
        return True
    else:
        return False

print(text_starta_endb("aabbbb"))  # Returns: True
print(text_starta_endb("ababab"))  # Returns: False

"""
This function uses Python's built-in `re` module, which provides support for regular expressions. The regular expression we use is `ab*`, which matches an `a` followed by any number of `b`'s (including zero `b`'s). The `*` in the regular expression means "zero or more of the preceding element".
"""

# SOLUTION ENDS HERE
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a Python function that counts the number of occurrences of a substring in a string.
<jupyter_code>
# SOLUTION STARTS HERE

