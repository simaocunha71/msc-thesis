def extract_values(s):
    import re
    return re.findall(r'"([^"]*)"', s)

print(extract_values('"Python",  "PHP",  "Java"'))

"""
The function works by using a regular expression to find all occurrences of text enclosed in quotation marks in the string. The regular expression r'"([^"]*)"' matches any sequence of characters that is not a quotation mark, within quotation marks.

The function re.findall returns a list of all matches found in the string.
"""

# Q2
