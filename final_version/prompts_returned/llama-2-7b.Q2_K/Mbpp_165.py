"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""
import re
def count_char_position(s):
    # add space counter for every character
    space = 1
    char_occurrence = []
    space_counter = 0
    s_re = "|".join([f'[{c:l}]' for c in list(set(s))] + ["|"])
    for m, group in re.finditer('({}|{})'.format(s_re), s):
        space += space_counter
        c_index = m.start() - 1 if m.group(0) == '' else int(m.group(0))
        c_occurrence = (m.group(1) + "|" * (space_counter - space)).rstrip("-") or ""
        char_occurrence += f'{c:l}{" " if not len(c_occurrence) else "-"}{" ".join([f"[{x:l}]" for x in c_index]) + str((len(s) - space_counter), ":", str(space_counter)) + " - |"}".format(repr(c_index)), )
        space += 1
    # sort alphabets in reverse order and print result
    re.sort(list(set(char_occurrence[:-1])), key=lambda x: list(set(x))[0] if type(list(set(x))) == set else -len(list(set(x))))
    return space, char_occurrence[space:-1]
print(count_char_position("cdefghi"))
