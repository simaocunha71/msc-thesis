
def move_num(s):
    chars = []
    nums = []
    for i in s:
        if i.isnumeric():
            nums.append(i)
        else:
            chars.append(i)
    return ''.join(chars + nums)

print(move_num('I1love143you55three3000thousand'))

# Output:
# Iloveyouthreethousand1143553000

"""
This function works by creating two lists: one for characters and one for numbers.
It iterates through the string, checking if each character is numeric.
If it is, it appends that number to the nums list, if not, it appends the character to the chars list.
Finally, it returns a string that is the concatenation of the chars list and nums list.
"""


"""
Here is another way to solve this problem using list comprehension and the sorted function.
"""

def move_num_2(s):
    return "".join(sorted(s, key=lambda x: x.isdigit()))

print(move_num_2('I1love143you55three3000thousand'))

# Output:
# Iloveyouthreethousand1143553000

"""
This function works in a similar way to the first, but it uses the sorted function with a custom key function.
The key function checks if each character is numeric and returns True if it is. This tells the sorted function to place all the numeric characters at the end of the string.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
