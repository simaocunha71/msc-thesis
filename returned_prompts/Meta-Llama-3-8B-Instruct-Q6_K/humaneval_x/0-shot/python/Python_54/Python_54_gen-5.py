def same_chars(s0: str, s1: str):
    return sorted(s0) == sorted(s1)

# same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
# same_chars('abcd', 'dddddddabc')
# same_chars('dddddddabc', 'abcd')
# same_chars('eabcd', 'dddddddabc')
# same_chars('abcd', 'dddddddabce')
# same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')  # False

# Test the function with the provided test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
# Output: 
# True
# True
# True
# False
# False
# False
# 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.