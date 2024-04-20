"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""

def remove_odd(s):
    for i in s:
        if(i % 2 == 1):
            del s[i]
print(remove_odd("Python"))