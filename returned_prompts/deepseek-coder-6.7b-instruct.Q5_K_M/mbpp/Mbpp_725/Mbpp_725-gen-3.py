
def extract_quotation(s):
    import re
    return re.findall(r'"([^"]*)"', s)

print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))

# The function uses the findall method from the re module to find all occurrences of a string that matches the given pattern. The pattern r'"([^"]*)"' finds all occurrences of a string that starts with a double quote, has any number of characters other than a double quote, and ends with a double quote. The parentheses in the pattern indicate a capture group, which means that the characters matched by the pattern are returned as part of the result.
<jupyter_output>
['A53', 'multi', 'Processor']
<jupyter_text>
Question 3:
<jupyter_code>
