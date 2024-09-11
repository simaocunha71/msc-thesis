"""
def extract_quotation(s):
    quotes = []
    while True:
        i = s.find('"')
        if i == -1:
            break
        j = s.find('"', i + 1)
        if j == -1:
            break
        quotes.append(s[i + 1: j])
        s = s[:i] + s[j:]
    return quotes

def test_extract_quotation():
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    print("All tests passed.")

test_extract_quotation()
"""

def extract_quotation(s):
    quotes = []
    while True:
        i = s.find('"')
        if i == -1:
            break
        j = s.find('"', i + 1)
        if j == -1:
            break
        quotes.append(s[i + 1: j])
        s = s[:i] + s[j:]
    return quotes

def test_extract_quotation():
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    print("All tests passed.")

test_extract_quotation()



"""
"""
def extract_quotation(s):
    quotes = []
    while True:
        i = s.find('"')
        if i == -1:
            break
        j = s.find('"', i + 1)
        if j == -1:
            break
        quotes.append(s[i + 1: j])
        s = s[:i] + s[j:]
    return quotes

def test_extract_quotation():
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    print("All tests passed.")

test_extract_quotation()
"""

"""
def extract_