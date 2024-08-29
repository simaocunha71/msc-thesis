
def replace_spaces(string: str):
    return string.replace(" ", "%20")

print(replace_spaces("My Name is Dawood"))

"""
This solution uses Python's built-in string method 'replace'. It replaces all occurrences of " " (a single space) with "%20".
"""

# Solution 2:

def replace_spaces(string: str):
    return "%20".join(string.split())

print(replace_spaces("My Name is Dawood"))

"""
This solution splits the original string at every space and rejoins them with "%20" in between. 
This is more efficient because it only traverses the string once.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
