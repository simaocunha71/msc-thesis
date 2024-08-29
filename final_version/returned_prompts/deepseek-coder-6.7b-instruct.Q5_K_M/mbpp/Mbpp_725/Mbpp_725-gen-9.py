def extract_quotation(s):
    return re.findall(r'"([^"]*)"', s)

print(extract_quotation('Cortex  "A53" Based  "multi" tasking  "Processor"'))
<jupyter_output>
['A53', 'multi', 'Processor']
<jupyter_text>
