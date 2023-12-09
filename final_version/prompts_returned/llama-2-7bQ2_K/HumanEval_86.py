
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

    if len(s) == 0:
        return s
    
    arr = list(map(lambda x: ord(x), s))   # list of ASCII values (ints)
    sorted_arr = sorted(arr, reverse=True)      # sort the ints in ascending order

    str_to_print = ""

    for i in range(0, len(sorted_arr)):
        str_to_print += chr((256 - sorted_arr[i]) % 256 + 1)  # print the character at the index
    
    return str_to_print
