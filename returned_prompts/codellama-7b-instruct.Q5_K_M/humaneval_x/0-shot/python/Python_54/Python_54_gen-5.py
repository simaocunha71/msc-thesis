
def same_chars(s0: str, s1: str):
    # s0 and s1 are the two strings to compare.
    # You can use any of the string methods
    # or any other methods you want.
    # Return True if the characters are the same
    # and False otherwise.
    # Hint: if you are not sure how to check
    # characters in a string, you can use the
    # string's index method.
    # The string's index method returns the
    # index of the first occurrence of a character
    # in the string.

    for i in s0:
        if s1.index(i) == -1:
            return False
    return True


