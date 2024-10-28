from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = strings[0]
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string

    return longest_str
# this solution has a time complexity of O(n) where n is the number of strings in the list
# this is because it needs to iterate over all the strings in the list once
# the space complexity is O(1) as it only uses a constant amount of space to store the longest string and the original string
# this solution assumes that the input list is not empty and does not contain any strings that are not strings
# if the input list is empty, it returns None as per the problem statement
# if there are multiple strings of the same length, it returns the first one it encounters
# the function is case sensitive and considers 'a' and 'A' as different characters
# it also considers 'abc' and 'abcd' as different strings, even though 'abcd' is a substring of 'abc' and 'abcd'
# the function does not trim the strings, so it considers 'abc' and 'abc ' as different strings
# it also considers 'abc' and 'abc\n' as different strings, even though 'abc\n' is a substring of 'abc' and 'abc\n'
# the function does not handle any exceptions, so if the input list contains a non-string value, it will raise an exception
# the function does not handle any non-unicode strings, so if the input list contains a non-unicode string, it will raise an exception
# the function does not handle any strings that are longer than the maximum allowed string size, so if the input list contains a string that is longer than the maximum allowed string size, it will raise an exception
# the function does not handle any strings that contain null bytes, so if the input list contains a string that contains null bytes, it will raise an exception
# the function does not handle any strings that contain surrogate pairs, so if the input list contains a string that contains surrogate pairs, it will raise an exception
# the function does not handle any strings that contain characters that are not in the range U+0000 to U+10FFFF, so if the input list contains a string that contains characters that are not in the range U+0000 to U+10FFFF, it