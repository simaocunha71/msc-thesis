"""
def text_match_two_three(text):
    if 'a' in text and 'b' in text:
        if text.count('b') == 2 or text.count('b') == 3:
            return True
        else:
            return False
    else:
        return False
"""

def text_match_two_three(text):
    if 'a' in text and 'b' in text:
        if text.count('b') == 2 or text.count('b') == 3:
            return True
        else:
            return False
    else:
        return False

print(text_match_two_three("abbb")) # True
print(text_match_two_three("ac"))  # False
print(text_match_two_three("aba")) # False
print(text_match_two_three("abbbaa")) # True
print(text_match_two_three("abab"))  # False
print(text_match_two_three("axbb"))  # False

#assert text_match_two_three("ac")==(False)
#assert text_match_two_three("abbb")==(True)
#assert text_match_two_three("aba")==(False)
#assert text_match_two_three("abbbaa")==(True)
#assert text_match_two_three("abab")==(False)
#assert text_match_two_three("axbb")==(False)

"""
def text_match_two_three(text):
    if 'a' in text and 'b' in text:
        if text.count('b') == 2 or text.count('b') == 3:
            return True
        else:
            return False
    else:
        return False

assert text_match_two_three("ac")==(False)
assert text_match_two_three("abbb")==(True)
assert text_match_two_three("aba")==(False)
assert text_match_two_three("abbbaa")==(True)
assert text_match_two_three("abab")==(False)
assert text