def move_num(s):
    chars = []
    nums = []
    for char in s:
        if char.isnumeric():
            nums.append(char)
        else:
            chars.append(char)
    return ''.join(chars+nums)

print(move_num('I1love143you55three3000thousand'))  # Iloveyouthreethousand1143553000

"""
Explanation:
- The function move_num takes a string as an argument.
- It then iterates over the string character by character.
- If the character is a number, it adds it to nums list.
- If the character is not a number, it adds it to chars list.
- Finally, it returns a new string that is the concatenation of chars and nums.
"""

"""
Test cases:
print(move_num('112Ilove143you55three3000thousand'))  # 'Iloveyouthreethousand1143553000112'
print(move_num('11111111111111111111111111111111'))  # '11111111111111111111111111111111'
print(move_num('a1b2c3'))  # 'abc321'
print(move_num('a1b2c3d4'))  # 'abcd4213'
"""
<jupyter_output>
Iloveyouthreethousand1143553000
<jupyter_text>
Question 3
<jupyter_code>
