def extract_values(s):
    import re
    return re.findall(r'"([^"]*)"', s)

print(extract_extract_values('"Python",  "PHP",  "Java"'))

# Output: ['Python', 'PHP', 'Java']

"""
Explanation:
The function uses the Python 're' module (regular expression) to find all substrings in the input string that are enclosed in double quotation marks. 
The regular expression '".*"', where '.*' represents any character other than a newline, is used to find such substrings. 
The function returns these substrings as a list.
"""
<jupyter_output>
['Python', 'PHP', 'Java']
<jupyter_text>
Problem 3
<jupyter_code>
