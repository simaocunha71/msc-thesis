"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""
import re
def extract_string(str_values, size):
    list_of_strings = []
    list_of_words = [""] + str_values.split()
    for i in range(0, len(list_of_words)):
        if (i+size) > 25:
            if(re.search(' ',str_values[i]):
                list_of_strings.append(str_values[i:i + size])
                i += size
            else:
                list_of_strings.append(str_values[i:])
        else:
            if(re.search(' ',str_values[i]):
                list_of_strings.append(str_values[i:i+size])
            else:
                list_of_strings.append(str_values[i:])
    return list_of_strings
print extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)