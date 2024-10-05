
    def odd_count(lst):
        result = []
        for i in range(len(lst)):
            count = sum(1 for c in lst[i] if int(c) % 2 != 0)
            result.append(f"the number of odd elements {count}n the str{count}ng {count} of the {count}nput.")
        return result

    print(odd_count(['1234567']))
    print(odd_count(['3',"11111111"]))



Output:

    ['the number of odd elements 4n the str4ng 4 of the 4nput.']
    ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 8n the str8ng 8 of the 8nput.']

"""


def odd_count(lst):
    result = []
    for i in range(len(lst)):
        count = sum(1 for c in lst[i] if int(c) % 2 != 0)
        result.append(f"the number of odd elements {count}n the str{count}ng {count} of the {count}nput.")
    return result

print(odd_count(['1234567']))
print(odd_count(['3',"11111111"]))
<jupyter_output>
['the number of odd elements 4n the str4ng 4 of the 4nput.']
['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 8n the str8ng 8 of the 8nput.']
<jupyter_text>
Problem 2: Create a function that returns the sum of all the digits of a number.
<jupyter_code>
"""
