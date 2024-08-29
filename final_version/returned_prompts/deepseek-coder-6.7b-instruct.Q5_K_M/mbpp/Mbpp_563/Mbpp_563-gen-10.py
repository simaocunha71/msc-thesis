def extract_values(s):
    return [i.strip('"') for i in s.split(',')]

print(extract_values('"Python",  "PHP",  "Java"'))

# Output: ['Python', 'PHP', 'Java']

# This function works by splitting the string at every comma, then removing any quotation marks from the resulting strings.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4
<jupyter_code>
