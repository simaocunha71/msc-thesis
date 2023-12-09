

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    distinct_chars = set()
    for c in string.lower():  # use lowercase letters to avoid 'a' vs 'A'.
        if c not in distinct_chars:  # make sure we don't count duplicates of the same character again and again
            distinct_chars.add(c)
    return len(distinct_chars)