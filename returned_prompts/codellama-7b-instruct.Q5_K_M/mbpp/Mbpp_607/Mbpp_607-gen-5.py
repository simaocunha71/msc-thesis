
import re

def find_literals(search_string, pattern):
    search_pattern = re.compile(pattern)
    found_literals = search_pattern.findall(search_string)
    if found_literals:
        found_literal = found_literals[0]
        start_index = search_string.index(found_literal)
        end_index = start_index + len(found_literal)
        return (found_literal, start_index, end_index)
    else:
        return (None, None, None)


