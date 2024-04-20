"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""

def replace_char(str, old, new):
    """ Replace the input character with the new one and return 
        the modified result. """
    if type(old) == str:
        # handle strings
        return [x for x in str.split() if x != old]
        
    elif type(new) == str:
        # handle lists
        return str[:len(str)] + [new] * (len(str) - len(old))