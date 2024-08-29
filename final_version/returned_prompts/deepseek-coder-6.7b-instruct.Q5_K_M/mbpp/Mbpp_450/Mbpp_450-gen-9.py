def extract_string(lst, size):
    return [word for word in lst if len(word) > size]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))
<jupyter_output>
['exercises', 'practice', 'solution']
<jupyter_text>
Q2:
<jupyter_code>
