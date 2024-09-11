def text_match_wordz_middle(string):
    # return True if 'z' is present in the string and not at the start or end
    # else return False
    if 'z' in string:
        if string[0] != 'z' and string[-1] != 'z':
            return True
    return False

# Test Case
print(text_match_wordz_middle("pythonzabc."))  # True
print(text_match_wordz_middle("zpythonz"))   # False
print(text_match_wordz_middle("aaz"))        # False
print(text_match_wordz_middle("abcza"))      # True
print(text_match_wordz_middle("za"))         # False




# Other Solution:
"""
def text_match_wordz_middle(string):
    if 'z' in string:
        if string[0] != 'z' and string[-1] != 'z':
            return True
    return False
"""
"""
def text_match_wordz_middle(string):
    if 'z' in string:
        if string.count('z') > 2:
            return True
    return False
"""
"""
def text_match_wordz_middle(string):
    return 'z' in string and string[0] != 'z' and string[-1] != 'z'
"""
"""
def text_match_wordz_middle(string):
    if 'z' in string:
        return True
    else:
        return False
"""
"""
def text_match_wordz_middle(string):
    if 'z' in string:
        if string[0] != 'z' and string[-1] != 'z':
            return True
    else:
        return False
"""
"""
def text_match_wordz_middle(string):
    if 'z' in string and len(string) > 2:
        if string[0] != 'z' and string[-1] != 'z':
            return True
    return False
"""


"""
def text_match_wordz_middle(string):
    if 'z' in string and len(