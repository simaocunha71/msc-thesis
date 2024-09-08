def text_match_two_three(text):
    if 'ab' in text or 'abc' in text:
        return True
    else:
        return False

# Test Cases
print(text_match_two_three("ac"))  # False
print(text_match_two_three("ab"))  # True
print(text_match_two_three("abc"))  # True
print(text_match_two_three("abbc"))  # True
print(text_match_two_three("acb"))  # False
print(text_match_two_three("abbbc"))  # True
print(text_match_two_three("abcd"))  # False

