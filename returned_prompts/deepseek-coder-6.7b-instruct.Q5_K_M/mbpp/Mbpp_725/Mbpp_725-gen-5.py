def extract_quotation(s):
    return [i for i in s.split() if i.startswith('"')]

print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))

