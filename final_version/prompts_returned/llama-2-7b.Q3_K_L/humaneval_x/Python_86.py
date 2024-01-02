
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    new_string = ""
    for i in s:  # Loop through each character of the given string.
        if len(new_string) > 0 and ord(i) < ord(new_string[-1]):  # If a word exists, then add it to the end else append it to the begining
            new_string += i  # Add the character to the end of the string.
        if len(new_string) > 0 and ord(i) == ord(new_string[-1]):  # If a word exists, then append it to the begining else add it to the end.
            new_string += i
    return new_string
