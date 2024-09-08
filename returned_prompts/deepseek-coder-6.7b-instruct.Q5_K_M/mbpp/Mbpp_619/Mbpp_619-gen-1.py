
def move_num(s):
    nums = [i for i in s if i.isdigit()]
    chars = [i for i in s if not i.isdigit()]
    chars.extend(nums)
    return "".join(chars)

print(move_num('I1love143you55three3000thousand')) # Iloveyouthreethousand1143553000

"""
Explanation:

Here, we are given a string containing both letters and numbers. We have to move all the numbers to the end of the string, while keeping the letters in the same order.

We use Python's list comprehension to separate the characters and numbers from the string and then we extend the list of characters with the list of numbers. Finally, we join the list back into a string and return it.
"""
<jupyter_output>
Iloveyouthreethousand1143553000
<jupyter_text>
Q2:
<jupyter_code>
