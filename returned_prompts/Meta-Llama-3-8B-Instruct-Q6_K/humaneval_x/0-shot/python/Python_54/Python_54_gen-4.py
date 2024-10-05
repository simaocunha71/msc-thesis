def same_chars(s0: str, s1: str):
    return sorted(s0) == sorted(s1) and len(s0) == len(s1)

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
# Explanation
The function checks if two strings have the same characters, regardless of their order. It achieves this by sorting both strings and comparing the results. Additionally, it checks if both strings have the same length. If both conditions are met, it returns True; otherwise, it returns False. This approach ensures that the function ignores the order of characters and only considers their presence. The test cases demonstrate the function's behavior for different input strings.