
def extract_quotation(s):
    result = []
    temp = ""
    is_quoted = False
    for ch in s:
        if ch == '"':
            is_quoted = not is_quoted
            if is_quoted:
                temp = ""
            else:
                result.append(temp)
        elif is_quoted:
            temp += ch
    return result

assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""

Here, we go through each character in the string. If the character is a quotation mark, we flip the 'is_quoted' flag. If 'is_quoted' is True, we start accumulating characters into 'temp'. When we encounter another quotation mark, we add the content of 'temp' to 'result' and reset 'temp'.
"""

# Task 3

