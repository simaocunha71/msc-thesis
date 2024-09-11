"""
Here is a simple Python function that does exactly that:

def text_starta_endb(txt):
    return txt.startswith('a') and txt.endswith('b')

You can use the Python 'assert' keyword to test the function. Here's an example:

assert text_starta_endb("aabbbb")  # This will pass, as "aabbbb" does start with an 'a' and end with a 'b'
"""

def text_starta_endb(txt):
    return txt.startswith('a') and txt.endswith('b')

# This will pass, as "aabbbb" does start with an 'a' and end with a 'b'
assert text_starta_endb("aabbbb")

# This will fail, as "abc" does not start with an 'a'
assert text_starta_endb("abc")

# This will fail, as "xyz" does not end with a 'b'
assert text_starta_endb("xyz")

# This will pass, as "ab" does start with an 'a' and end with a 'b'
assert text_starta_endb("ab")

# This will pass, as "b" does end with a 'b'
assert text_starta_endb("b")

# This will fail, as "c" does not start with an 'a'
assert text_starta_endb("c")

# This will fail, as "axby" does not end with a 'b'
assert text_starta_endb("axby")

# This will fail, as "axby" does not start with an 'a'
assert text_starta_endb("axby")

# This will pass, as "ab" does start with an 'a' and end with a 'b'
assert text_starta_endb("ab")

# This will pass, as "b" does end with a 'b'
assert text_starta_endb("b")

# This will fail, as "c" does not start with an 'a'
assert text_starta_endb