"""
def text_match_wordz_middle(str):
    # check if the string is empty
    if len(str) == 0:
        return False
    # check if the first and last character of the string is 'z'
    if str[0] == 'z' and str[-1] == 'z':
        # if yes, check if the remaining characters are not 'z'
        for i in range(1, len(str)-1):
            if str[i] == 'z':
                return False
        return True
    return False
"""

def text_match_wordz_middle(str):
    return 'z' in str and str[0] != 'z' and str[-1] != 'z'

# test
print(text_match_wordz_middle("pythonzabc.")) # True
print(text_match_wordz_middle("zpythonzabc.")) # False
print(text_match_wordz_middle("zpythonz")) # False
print(text_match_wordz_middle("pythonz")) # True
print(text_match_wordz_middle("")) # False

```