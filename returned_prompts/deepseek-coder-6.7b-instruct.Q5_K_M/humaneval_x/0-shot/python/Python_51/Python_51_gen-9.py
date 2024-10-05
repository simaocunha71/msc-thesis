
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    no_vowels = ""
    for char in text:
        if char not in vowels:
            no_vowels += char
    return no_vowels
"""

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'

# Output:
# ''
# 'bcdf\nghjklm'
# 'bcdf'
# ''
# 'B'
# 'zbcd'
"""
<jupyter_output>
''
'bcdf
ghjklm'
'bcdf'
''
'B'
'zbcd'
<jupyter_text>
Task 2: String Formatting (4 points)Write a function `format_string` that takes a string and a width as input parameters. The function should return a new string where the original string is padded with spaces on both sides so that it is centered within a field of specified width. If the width is less than the length of the original string, the original string is returned unchanged. The spaces are added after the string so that the total width of the string is the specified width.
<jupyter_code>
def format_string(s, width):
    """
    format_string is a function that takes a string and a width as input parameters.
    The function returns a new string where the original string is padded with spaces on both sides 
    so that it is centered within a field of specified width.
    If the width is less than the length of the original string,
    the original string is returned unchanged.
    The spaces are added after the string so that the total width of the