
def check_if_last_char_is_a_letter(txt):
    if not txt or not txt[-1].isalpha():
        return False
    if len(txt) == 1:
        return True
    return not txt[-2].isalpha()

print(check_if_last_char_is_a_letter("apple pie")) # False
print(check_if_last_char_is_a_letter("apple pi e")) # True
print(check_if_last_char_is_a_letter("apple pi e  ")) # False
print(check_if_last_char_is_a_letter("")) # False

# this function works by checking if the last character of the string is an alphabetical character and if the character before it is not.
# if the string is empty or if the last character is not alphabetical, it returns False.
# if the string only has one character, it returns True.
# otherwise, it checks if the character before the last one is alphabetical and returns the opposite of that.
<jupyter_output>
False
True
False
False
<jupyter_text>
**Q2:**Write a function that takes a list of lists and flattens it into a one-dimensional list. Name the function `flatten`.For example, given the input `[[1, 2], [3, 4]]`, the function should return `[1, 2, 3, 4]`.
<jupyter_code>
