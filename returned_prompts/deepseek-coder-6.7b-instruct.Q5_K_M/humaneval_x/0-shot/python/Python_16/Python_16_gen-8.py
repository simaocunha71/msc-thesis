

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))


if __name__ == '__main__':
    import doctest
    doctest.testmod()


Explanation:

In Python, the `set` data type is an unordered collection of unique elements. The `string.lower()` function is used to convert the string to lowercase (since we are considering case-insensitive characters), and `len(set(...))` is used to count the number of unique characters in the string.


Alternative solution:

You can also solve this problem by using a dictionary to count the occurrence of each character, and then return the length of the dictionary.


def count_distinct_characters(string: str) -> int:
    char_count = {}
    for char in string.lower():
        if char not in char_count:
            char_count[char] = 1
    return len(char_count)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''

# Solution 3:
'''
