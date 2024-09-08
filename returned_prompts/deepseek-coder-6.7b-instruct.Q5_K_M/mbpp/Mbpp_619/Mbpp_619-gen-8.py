def move_num(s):
    letters = []
    numbers = []
    for i in s:
        if i.isalpha():
        # if i.isdigit() == False:
            letters.append(i)
        else:
            numbers.append(i)
    return ''.join(letters+numbers)

print(move_num('I1love143you55three3000thousand'))


"""
Another solution using re module
"""

import re

def move_num(s):
    letters = re.sub(r'[0-9]', '', s)
    numbers = re.sub(r'[a-zA-Z]', '', s)
    return letters + numbers

print(move_num('I1love143you55three3000thousand'))

# Both will return: Iloveyouthreethousand1143553000
<jupyter_output>
Iloveyouthreethousand1143553000
Iloveyouthreethousand1143553000
<jupyter_text>
