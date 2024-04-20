"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""

def extract_string(strings, length):
    result = []   # to store the required string

    for s in strings:    # Loop through each element in the list.
        if len(s) > length:    # If the length of string is greater than given length.
            rest_string = s[:length]  # Extract the required string from the input list.
            break               # Break out of the loop.
        else : result.append(rest_string)      # Else append all strings to result list.
    return result       # Return the extracted string.
print extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)