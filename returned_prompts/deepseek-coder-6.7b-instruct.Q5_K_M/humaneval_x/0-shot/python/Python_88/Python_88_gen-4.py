
    if len(array) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

print(sort_array([]))
print(sort_array([5]))
print(sort_array([2, 4, 3, 0, 1, 5]))
print(sort_array([2, 4, 3, 0, 1, 5, 6]))
<jupyter_output>
[]
[5]
[0, 1, 2, 3, 4, 5]
[6, 5, 4, 3, 2, 1, 0]
<jupyter_text>
**Question 2**Given a string, compute recursively a new string where all the 'x' chars have been removed.For example, if the input is "xhixhix", the output should be "hihi".
<jupyter_code>
def remove_x(string):
    if not string:
        return string
    else:
        return string.replace('x', '')

print(remove_x("xhixhix"))
<jupyter_output>
hihi
<jupyter_text>
**Question 3**Given a string, compute recursively a new string where all the adjacent chars are two chars far. For example, if the input is "abc", the output should be "cab".
<jupyter_code>
def two_chars_far(string):
    if len(string) < 3:
        return string
    else:
        return string[2:] + string[:2]

print(two_chars_far("abc"))
<jupyter_output>
cab
<jupyter_text>
**Question 4**Given a string, compute recursively a new string where all the 'p' chars have been replaced by 't'.For example, if the input is "top", the output should be "tot".
<jupyter_code>
def replace_p(string):
    if not string:
        return string
    else:
        return string.replace('p