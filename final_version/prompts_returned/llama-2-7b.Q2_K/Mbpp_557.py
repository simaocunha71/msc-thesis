"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""

def toggle_string(s):
    for c in s:
        if str(c).isupper():
            res = str(c) + "t"
        elif str(c).islower():
            res = str(c) + "T"
        else:
            res = str(c)
        print(res)
        s += res
    return s
