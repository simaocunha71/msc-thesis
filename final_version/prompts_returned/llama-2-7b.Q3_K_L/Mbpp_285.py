"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
def text_match_two_three(text):
    if text[0:2]=="ab":
        return True
    elif text[0:3]="aaa":
        return True
    else:
        return False