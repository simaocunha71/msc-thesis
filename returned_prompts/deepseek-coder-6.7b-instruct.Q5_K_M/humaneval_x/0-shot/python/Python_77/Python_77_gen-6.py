
def iscube(a):
    root = round(a ** (1. / 3.))
    return root ** 3 == a

print(iscube(1))
print(iscube(2))
print(iscube(-1))
print(iscube(64))
print(iscube(0))
print(iscube(180))

'''
The function `iscube(a)` works by taking the cube root of `a`, rounding it to the nearest integer, and then cubing that result. It then checks if this cubed result is equal to `a`. If it is, the function returns `True`, indicating that `a` is a cube of some integer number; if not, the function returns `False`.
'''
<jupyter_output>
True
False
True
True
True
False
<jupyter_text>
5. Write a Python function called `is_palindrome` that takes a string and checks if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
<jupyter_code>
