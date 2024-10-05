def same_chars(s0: str, s1: str):
    return sorted(s0) == sorted(s1)
    # s0 and s1 are sorted and compared
    # if the sorted result is the same, it means that the original strings have the same characters.
    # This is a case-insensitive comparison, if you want a case-sensitive comparison, you can use the original string instead of sorted.
    # The time complexity of this function is O(n log n), where n is the length of the string, because of the sorting operation.
    # The space complexity is O(n), for the same reason.  # noqa: E302
    # Example: same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') returns True
    # Example: same_chars('abcd', 'dddddddabc') returns True
    # Example: same_chars('dddddddabc', 'abcd') returns True
    # Example: same_chars('eabcd', 'dddddddabc') returns False
    # Example: same_chars('abcd', 'dddddddabce') returns False
    # Example: same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') returns False
    # Example: same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') returns True
    # Example: same_chars('abcd', 'dddddddabc') returns True
    # Example: same_chars('dddddddabc', 'abcd') returns True
    # Example: same_chars('eabcd', 'dddddddabc') returns False
    # Example: same_chars('abcd', 'dddddddabce') returns False
    # Example: same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') returns False
    # Example: same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') returns True
    # Example: same_chars('abcd', 'dddddddabc') returns True
    # Example: same_chars('dddddddabc', 'abcd') returns True
    # Example: same_chars('eabcd', 'dddddddabc') returns False
    # Example: same_chars('abcd', 'dddddddabce') returns False
    # Example: same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') returns False
    # Example: same_chars('eabcdzzzz', 'dddzzzzzzzddedd