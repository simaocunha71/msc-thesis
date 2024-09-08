def concatenate_tuple(t):
    return '-'.join(str(x) for x in t)

print(concatenate_tuple(("ID", "is", 4, "UTS")))

# Output:
# ID-is-4-UTS

# Explanation:
# The function 'concatenate_tuple' takes a tuple as input. It uses the 'join' method to concatenate the elements of the tuple. The elements are first converted to a string using the 'str' function and then joined by the '-' delimiter. The resulting string is returned.
<jupyter_output>
ID-is-4-UTS
<jupyter_text>
Question 2
<jupyter_code>
