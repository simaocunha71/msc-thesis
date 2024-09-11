"""
def extract_quotation(s):
    s = s.split(" ")
    res = []
    for i in s:
        if i.startswith("\"") and i.endswith("\""):
            res.append(i[1:-1])
    return res


print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
"""

def extract_quotation(s):
    return [i[1:-1] for i in s.split(' ') if i[0]=='"' and i[-1]=='"']

print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))



"""
"""


def extract_quotation(s):
    s = s.split(' ')
    res = []
    for i in s:
        if i.startswith('"') and i.endswith('"'):
            res.append(i[1:-1])
    return res

print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))




"""
"""
def extract_quotation(s):
    res = []
    i = 0
    while i < len(s):
        if s[i] == '"':
            if i != len(s) - 1 and s[i+1] == '"':
                res.append(s[i+1:].split('"', 1)[0])
                i += 2
            else:
                res.append(s[i:].split('"', 1)[0])
                i += 1
        else:
            i += 1
    return res

print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
"""

"""
def extract_quotation(s):
    res = []
    i = 0
    while i < len(s):
        if s[i] == '"':
            if i != len(s) - 1 and s[i+1] == '"':
                res