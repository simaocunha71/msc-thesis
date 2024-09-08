def add_string(lst, string):
    return [string.format(i) for i in lst]

print(add_string([1,2,3,4],'temp{0}'))

# Output: ['temp1', 'temp2', 'temp3', 'temp4']

# Explanation:
# The function add_string takes in a list and a string.
# It applies the string format method to each element in the list.
# The {0} in the string is a placeholder for the element's value.
# The format method replaces the {0} with the element's value, creating a new string for each element.
# The function returns a new list with these new strings.

# Testing with other inputs:
print(add_string(['a', 'b', 'c'], 'test{0}'))  # Output: ['testa', 'testb', 'testc']
print(add_string([5, 10, 15, 20], 'num{0}'))  # Output: ['num5', 'num10', 'num15', 'num20']
<jupyter_output>
['temp1', 'temp2', 'temp3', 'temp4']
['testa', 'testb', 'testc']
['num5', 'num10', 'num15', 'num20']
<jupyter_text>
Question 3
<jupyter_code>
