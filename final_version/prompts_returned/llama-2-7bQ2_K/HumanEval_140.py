
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    
    if len(text) > 0:
        for i in text:  # for each character of the string s, replace all spaces in it with underscores.
            print(i, end='')
        return ''.join(['_' + x[1:] if len(x) == 2 and (len(x)) > 0 else '_' + x[1:]) for i in text] # for each character of the string s, replace all consecutive spaces with -.
    return ''
