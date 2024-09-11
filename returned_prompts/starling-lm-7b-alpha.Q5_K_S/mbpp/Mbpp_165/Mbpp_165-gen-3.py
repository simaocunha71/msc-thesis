def count_char_position(s):
    return sum(1 for i, c in enumerate(s.lower()) if ord(c) - i == ord('a'))

def test_count_char_position():
    assert count_char_position("xbcefg") == 2
    print("All tests passed.")

test_count_char_position()



"""
def count_char_position(s):
    # Convert the string to lowercase and initialize a counter to 0
    s_lower = s.lower()
    count = 0
    # Iterate through the string using the enumerate function
    for i, c in enumerate(s_lower):
        # Check if the character is an alphabet and if the index of the character is the same as the ASCII value of the character
        if c.isalpha() and ord(c) - i == ord('a'):
            # Increment the counter by 1
            count += 1
    # Return the counter
    return count
"""

"""
def test_count_char_position():
    assert count_char_position("xbcefg") == 2
    print("All tests passed.")

test_count_char_position()
"""



"""
def count_char_position(s):
    # Convert the string to lowercase and initialize a counter to 0
    s_lower = s.lower()
    count = 0
    # Iterate through the string using the enumerate function
    for i, c in enumerate(s_lower):
        # Check if the character is an alphabet and if the index of the character is the same as the ASCII value of the character
        if c.isalpha() and ord(c) - i == ord('a'):
            # Increment the counter by 1
            count += 1
    # Return the counter
    return count
"""


"""
def test_count_char_position():
    assert count_char_position("xbcefg") == 2
    print("All tests passed.")

test_count_char_position()
"""

"""
def count_char_position(s):
    # Convert the string to lowercase and initialize a