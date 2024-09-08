def move_num(s):
    num = [i for i in s if i.isdigit()]
    alpha = [i for i in s if not i.isdigit()]
    return ''.join(alpha + num)


print(move_num('I1love143you55three3000thousand'))  # 'Iloveyouthreethousand1143553000'

# Alternative Solution
def move_num(s):
    return ''.join(sorted(s, key=lambda x: x.isdigit()))


print(move_num('I1love143you55three3000thousand'))  # 'Iloveyouthreethousand1143553000'

"""
Explanation:
We can solve this problem by using Python built-in functions. 
1. We can use list comprehension to separate the digits and the letters in the string.
2. Then, we can concatenate the letters and numbers together and return the result.
"""

# Alternative Solution
def move_num(s):
    nums = []
    chars = []
    for c in s:
        if c.isdigit():
            nums.append(c)
        else:
            chars.append(c)
    return ''.join(chars + nums)


print(move_num('I1love143you55three3000thousand'))  # 'Iloveyouthreethousand1143553000'

"""
Explanation:
We can solve this problem by using Python built-in functions. 
1. We can iterate over each character in the string.
2. If the character is a digit, we append it to the `nums` list.
3. If the character is not a digit, we append it to the `chars` list.
4. Finally, we concatenate the `chars` and `nums` lists and return the result.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 4