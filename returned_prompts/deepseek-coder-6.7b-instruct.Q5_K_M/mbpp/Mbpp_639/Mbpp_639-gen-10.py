def sample_nam(names):
    return sum(len(name) for name in names if not name[0].islower())

assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16

Explanation:
The function sample_nam takes a list of names as input. It uses a generator expression to iterate over the names in the list. The expression checks if the first letter of each name (name[0]) is lowercase (not name[0].islower()). If the first letter is not lowercase, it adds the length of the name to the sum. The sum of lengths is returned as the result.

The sum of lengths of the names ['Dylan', 'Diana', 'Joanne'] is 16 (len('Dylan') + len('Diana') + len('Joanne'))
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
