def extract_values(s):
    import re
    matches = re.findall(r'"([^"]*)"', s)
    return matches

print(extract_values('"Python",  "PHP",  "Java"'))

# OUTPUT: ['Python', 'PHP', 'Java']

# Explanation:
# This function uses Python's regular expression (re) module to find all substrings that are enclosed in quotation marks. 
# The pattern r'"([^"]*)"' matches any string that is enclosed in quotation marks and captures the string inside the quotation marks.
<jupyter_output>
['Python', 'PHP', 'Java']
<jupyter_text>
