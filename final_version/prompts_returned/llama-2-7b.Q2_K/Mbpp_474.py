"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""

def replace_char(str, old, new):
    if (old+new) not in str:
        return str+" "+str[0].lower()+(str[1:])
    else:
        return str

print(replace_char("polygon",'y','l'))