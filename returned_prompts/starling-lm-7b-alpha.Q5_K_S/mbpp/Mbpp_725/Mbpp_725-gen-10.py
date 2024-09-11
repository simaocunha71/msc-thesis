"""
def extract_quotation(sentence):
    quote_list = []
    i = 0
    while i < len(sentence):
        if sentence[i] == '"':
            quote_list.append(sentence[i+1:].split('"')[0])
            i += 1
        i += 1
    return quote_list
"""

def extract_quotation(sentence):
    quote_list = []
    while " " in sentence:
        start = sentence.index(" ")
        end = sentence.rindex(" ")
        quote_list.append(sentence[start+1:end])
        sentence = sentence[end+1:]
    return quote_list

extract_quotation('Cortex "A53" Based "multi" tasking "Processor"')


# Testcase:
# Cortex "A53" Based "multi" tasking "Processor"
# Expected Result: ['A53', 'multi', 'Processor']

# Testcase:
# Cortex "A53" Based "multi" tasking "Processor"
# Expected Result: ['A53', 'multi', 'Processor']

# Testcase:
# Cortex "A53" Based "multi" tasking "Processor"
# Expected Result: ['A53', 'multi', 'Processor']

# Testcase:
# Cortex "A53" Based "multi" tasking "Processor"
# Expected Result: ['A53', 'multi', 'Processor']

# Testcase:
# Cortex "A53" Based "multi" tasking "Processor"
# Expected Result: ['A53', 'multi', 'Processor']

# Testcase:
# Cortex "A53" Based "multi" tasking "Processor"
# Expected Result: ['A53', 'multi', 'Processor']

# Testcase:
# Cortex "A53" Based "multi" tasking "Processor"
# Expected Result: ['A53', 'multi', 'Processor']

# Testcase:
# Cortex "A53" Based "multi" tasking "Processor"
# Expected Result: ['A5