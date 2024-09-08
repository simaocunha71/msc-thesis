def text_starta_endb(text):
    pattern = re.compile(r'a.*b$')
    if pattern.match(text):
        return True
    else:
        return False

print(text_starta_endb("aabbbb"))

#Q2
"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b', 
and has a length of 5.
assert text_starta_endb("aaaaab")
"""

A2:
def text_starta_endb(text):
    pattern = re.compile(r'a.*b$')
    if pattern.match(text) and len(text) == 5:
        return True
    else:
        return False

print(text_starta_endb("aaaaab"))

#Q3
"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b', 
and has a length of 5 to 10.
assert text_starta_endb("aaaaab")
assert text_starta_endb("aaaaaaaaab")
assert not text_starta_endb("aaaaaaaaaaab")
"""

A3:
def text_starta_endb(text):
    pattern = re.compile(r'a.*b$')
    if pattern.match(text) and 5 <= len(text) <= 10:
        return True
    else:
        return False

print(text_starta_endb("aaaaab"))
print(text_starta_endb("aaaaaaaaab"))
print(text_starta_endb("aaaaaaaaaaab"))

#Q4
"""
Write a function that matches a string that has an 'a' followed by exactly 2 'b's, ending in 'c'.
assert text_starta_endb("aabbc")
assert not text_starta_endb("aabbcc")
"""

A4:
def text_starta_endb(text):
    pattern = re.compile(r'aabb.c$')
    if pattern.match(text):
        return True
   