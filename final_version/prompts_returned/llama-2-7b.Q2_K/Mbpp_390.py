"""
Write a function to apply a given format string to all of the elements in a list.
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""
import re

def add_string(lst, format_str):  # 1. Write a function declaration header
    """applies a given format string to all of the elements in a list."""
    result = []
    for item in lst:
        s = str(item)
        formatted_s = re.sub(r'(\d{2})', r' \1 ', s)
        result.append(formatted_s)  # 2. Add an element to the list object (lst)
    return result

print add_string([1,2,3,4], 'temp%d')
# Output: ['temp1', 'temp2', 'temp3', 'temp4']