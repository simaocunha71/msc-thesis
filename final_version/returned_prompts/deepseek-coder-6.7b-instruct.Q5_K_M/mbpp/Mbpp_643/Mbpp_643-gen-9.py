def text_match_wordz_middle(text):
    import re
    pattern = "^[^z]*z[^z]*$"
    if re.search(pattern, text):
        return True
    else:
        return False

print(text_match_wordz_middle("pythonzabc."))

"""
In the above code, ^[^z]*z[^z]*$ matches any string that starts with any number of characters that are not 'z', followed by 'z' and then followed by any number of characters that are not 'z'. The ^ and $ ensure that 'z' is not at the start or the end of the string. The function then returns True if the string matches the pattern and False otherwise.
"""

# 2.
