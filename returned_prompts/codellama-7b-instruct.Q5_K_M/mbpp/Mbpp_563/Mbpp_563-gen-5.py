```
def extract_values(string):
    quotation_marks = string.count('"')
    values = []
    current_value = ''
    for i, char in enumerate(string):
        if char == '"':
            if quotation_marks % 2 == 1:
                values.append(current_value)
                current_value = ''
            else:
                current_value += char
            quotation_marks -= 1
    return values
```
