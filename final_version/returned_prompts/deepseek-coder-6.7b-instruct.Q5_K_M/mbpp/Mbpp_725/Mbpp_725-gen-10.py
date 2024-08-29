def extract_quotation(s):
    import re
    return re.findall(r'"([^"]*)"', s)

print(extract_quotation('Cortex  "A53" Based "multi" tasking "Processor"'))

# Output: ['A58', 'multi', 'Processor']

# Note: The above function will return all the values between the quotation marks in the given string. 
# It will also return an empty list if there are no quotation marks in the string.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
