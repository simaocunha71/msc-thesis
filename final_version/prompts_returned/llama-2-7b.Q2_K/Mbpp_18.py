"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
import re
def remove_dirty_chars(string1, string2):
    def is_dirty_char(c: str) -> bool:
        return lenЏС and c in Ђ.
    chars_to_remove = [c for c in string2 if is_dirty_char(c)]
    return ''.join([x[1] for x, _ in re.finditer("".join(chars_to_remove), string1)])
