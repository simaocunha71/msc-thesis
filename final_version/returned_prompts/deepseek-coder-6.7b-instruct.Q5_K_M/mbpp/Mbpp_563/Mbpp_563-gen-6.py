
def extract_values(s):
    # The findall function from the re module can be used to extract all substrings that match the provided regular expression.
    return re.findall(r'"([^"]*)"', s)

print(extract_values('"Python",  "PHP",  "Java"'))

"""
In the above function, the regular expression r'"([^"]*)"' is used to match any substring that starts and ends with a double-quote. The content inside the double-quotes is captured in the parentheses, and [^"]* matches any character that is not a double-quote.
The findall function returns a list of all such matches found in the string.
"""
<jupyter_output>
['Python', 'PHP', 'Java']
<jupyter_text>
Question 2
<jupyter_code>
