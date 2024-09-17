import re
def move_num(s):
    # Find all the numbers in the string using a regular expression pattern
    nums = re.findall(r'\d+', s)

    # Remove the numbers from the original string
    s = s.replace(*nums)

    # Concatenate the original string without the numbers and the list of numbers at the end
    return s.join(nums)