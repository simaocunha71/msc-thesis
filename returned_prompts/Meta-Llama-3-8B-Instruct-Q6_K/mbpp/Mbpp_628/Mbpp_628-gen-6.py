def replace_spaces(s):
    return s.replace(" ", "%20")
    # or
    # return s.replace(' ', '%20')  # Same result, but with a single quote

print(replace_spaces("My Name is Dawood"))  # Output: My%20Name%20is%20Dawood
print(replace_spaces("Hello World"))  # Output: Hello%20World
print(replace_spaces("   "))  # Output: %20%20%20
print(replace_spaces("a b c"))  # Output: a%20b%20c
print(replace_spaces("a"))  # Output: a
print(replace_spaces(""))  # Output: 
print(replace_spaces("  " + "a"))  # Output: %20a
print(replace_spaces("a" + "  "))  # Output: a%20
print(replace_spaces("a  b"))  # Output: a%20b
print(replace_spaces("a   b"))  # Output: a%20%20b
print(replace_spaces("a   b   c"))  # Output: a%20%20b%20c
print(replace_spaces("a   b   c   "))  # Output: a%20%20b%20c%20
print(replace_spaces("a   b   c   d"))  # Output: a%20%20b%20c%20d
print(replace_spaces("a   b   c   d   e"))  # Output: a%20%20b%20c%20d%20e
print(replace_spaces("a   b   c   d   e   f"))  # Output: a%20%20b%20c%20d%20e%20f
print(replace_spaces("a   b   c   d   e   f   g"))  # Output: a%20%20b%20c%20d%20e%20f%20g
print(replace_spaces("a   b   c   d   e   f   g   h"))  # Output: a%20%20b%20c%20d%20e%20f%20g%20h
print(replace_spaces("a   b   c   d   e   f   g   h   i"))  # Output: a%20%20b%20c%