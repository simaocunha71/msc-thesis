

import collections
import string

def count_distinct_characters(string):
    """
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert to lowercase
    string = string.lower()
    # Remove all the special characters
    string = string.translate(None, string.maketrans('', '', string.punctuation))
    # Use collections.Counter to count the distinct characters
    return len(collections.Counter(string).keys())
