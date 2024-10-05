def same_chars(s0: str, s1: str):
    return sorted(s0) == sorted(s1)
    # or 
    # return set(s0) == set(s1)
    # or 
    # return Counter(s0) == Counter(s1)

# Explanation:
# The function checks if the two input strings have the same characters, regardless of their order and frequency.
# It uses the sorted function to sort the characters in each string, and then compares the sorted lists.
# If the sorted lists are equal, the function returns True, indicating that the two strings have the same characters.
# If the sorted lists are not equal, the function returns False.

# For example, the inputs 'eabcdzzzz' and 'dddzzzzzzzddeddabc' have the same characters, so the function returns True.
# The inputs 'abcd' and 'dddddddabc' also have the same characters, so the function returns True.
# The inputs 'eabcd' and 'dddddddabc' do not have the same characters, so the function returns False.
# The inputs 'abcd' and 'dddddddabce' do not have the same characters, so the function returns False.
# The inputs 'eabcdzzzz' and 'dddzzzzzzzddddabc' do not have the same characters, so the function returns False.