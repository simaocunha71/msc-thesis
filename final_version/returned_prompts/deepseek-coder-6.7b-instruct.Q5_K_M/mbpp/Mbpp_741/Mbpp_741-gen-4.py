def all_Characters_Same(string):
    return len(set(string)) == 1

print(all_Characters_Same("python"))

# Solution:
# The function `all_Characters_Same` takes a string as an argument. It converts the string into a set which removes all duplicate characters. If the length of the set is 1, that means all characters in the string are same. It returns `True` in such case, else `False`.

# In the given example, the string "python" has all characters different. So, the function will return `False`.

# Note: The set function doesn't maintain the order of the elements. So, it may return `False` even if all characters in the string are same but in different order. If you want to check whether all characters are same and in the same order, use the following code:

def all_Characters_Same(string):
    return all(c == string[0] for c in string)

print(all_Characters_Same("python"))

# In the given example, the string "python" has all characters different. So, the function will return `False`.
<jupyter_output>
False
<jupyter_text>
Problem 2
<jupyter_code>
