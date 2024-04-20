"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
text_match_two_three = lambda x: (x.count('ab') and len(x) > 2) \
                            or (not x.count('a') and len(x) == 3)

