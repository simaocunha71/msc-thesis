def concatenate_tuple(t):
    return '-'.join(map(str, t))

print(concatenate_tuple(("ID", "is", 4, "UTS")))

#output: ID-is-4-UTS

Explanation:
The function `concatenate_tuple` takes a tuple `t` as an argument.
The `map` function applies the `str` function to all elements of the tuple, converting them all to strings.
The `join` method then concatenates these strings together with the `'-'` delimiter. The result is a single string with all the elements of the tuple joined by the `'-'` delimiter.
"""

#test
assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'
assert concatenate_tuple(("Hello", "World")) == 'Hello-World'
assert concatenate_tuple(("Python", "Programming", 101)) == 'Python-Programming-101'
print("All tests passed.")
<jupyter_output>
ID-is-4-UTS
Hello-World
Python-Programming-101
All tests passed.
<jupyter_text>
**Problem 2**
<jupyter_code>
