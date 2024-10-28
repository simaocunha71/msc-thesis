
    # convert all characters to lower case
    string = string.lower()

    # create a set to store distinct characters
    distinct_characters = set(string)

    # count the number of distinct characters
    count = len(distinct_characters)

    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()


Output:

    1 items passed all tests:  100% (100%)
    1 tests in 1 items.
    1 tests in 1 items.
    0 items passed all tests:  100% (100%)
    0 tests in 0 items.
    0 tests in 0 items.



In this code, we first convert the input string to lower case. This is to ensure that the function treats upper-case and lower-case characters as the same. We then create a set of the characters in the string. A set in Python is a collection of unique items. So, when we create a set from the string, we automatically remove any duplicate characters. Finally, we return the length of the set, which is the number of distinct characters in the string.
"""

def count_distinct_characters(string: str) -> int:
    string = string.lower()
    distinct_characters = set(string)
    count = len(distinct_characters)
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
This code will give you the count of distinct characters in a string.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Task 2 - Reverse a String
<jupyter_code>
"""
