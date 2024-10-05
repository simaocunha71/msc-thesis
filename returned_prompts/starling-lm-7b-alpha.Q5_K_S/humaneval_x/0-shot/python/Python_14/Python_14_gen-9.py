    prefixes = []
    for length in range(1, len(string) + 1):
        prefixes.append(string[:length])
    return prefixes


    # Substrings of a string are the string itself and all of its parts.
    # For example, the substrings of "abc" are "abc", "ab", "ac", "a", and "b".
    # The prefixes of a string are the first n-1 (n > 0) substrings of the string.
    # For example, the prefixes of "abc" are "a", "ab", and "abc".

    # Here's a step-by-step explanation of the code:

    # The variable prefixes is initialized as an empty list. This is where we will store each prefix as we create it.

    # We use a for loop to iterate through a range of values from 1 to the length of the input string plus 1. This range represents the lengths of all possible prefixes of the string.

    # Inside the loop, we use string slicing to extract the substring starting at index 0 and ending at index length (exclusive) from the input string. This substring is a prefix of the original string.

    # We then append this prefix to the prefixes list.

    # After the loop finishes, we have created all the prefixes of the string and stored them in the prefixes list. We return this list as the result.





def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['a', 'ab', 'abc']
    """

    suffixes = []
    for length in range(1, len(string) + 1):
        suffixes.append(string[-length:])
    return suffixes


    # Substrings of a string are the string itself and all of its parts.
    # For example, the substrings of "abc" are "abc", "ab", "ac", "a", and "b".
    # The suffixes of a string are the last n-1 (n > 0) substrings of the string