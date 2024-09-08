
def extract_quotation(s):
    import re
    return re.findall(r'"([^"]*)"', s)

print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
<jupyter_output>
['A53', 'multi', 'Processor']
<jupyter_text>
Question 2
<jupyter_code>
