def text_match_wordz_middle(text):
    import re
    if re.search(r'z[a-z]*z', text) and not re.search(r'^z|z$', text):
        return True
    else:
        return False

print(text_match_wordz_middle("pythonzabc."))  # True
print(text_match_wordz_middle("pythonabc."))  # False
print(text_match_wordz_middle("zpythonabcz"))  # False
print(text_match_wordz_middle("zpythonzabc.z"))  # True
print(text_match_wordz_middle("pythonz.abc"))  # False

"""
The function uses regular expressions to search for patterns. It looks for a 'z' followed by any number of letters (including none), followed by another 'z'. The '^' symbol is used to specify the start of the line, and the '$' symbol is used to specify the end of the line. 
The function will return True if the pattern is found and it's not at the start or end of the line. Otherwise, it will return False.
"""

# Other way to do this
def text_match_wordz_middle(text):
    return 'z' in text[1:-1]

print(text_match_wordz_middle("pythonzabc."))  # True
print(text_match_wordz_middle("pythonabc."))  # False
print(text_match_wordz_middle("zpythonabcz"))  # False
print(text_match_wordz_middle("zpythonzabc.z"))  # True
print(text_match_wordz_middle("pythonz.abc"))  # False

"""
This function works by checking if 'z' is in the string between the first and last character. It slices the string to exclude the first and last characters before checking for 'z'.
"""
<jupyter_output>
True
False
False
True
False
<jupyter_text>
