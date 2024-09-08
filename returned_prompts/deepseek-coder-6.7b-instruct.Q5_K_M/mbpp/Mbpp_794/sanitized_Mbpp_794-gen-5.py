def text_starta_endb(txt):
    # Python's built-in regex module re is used here.
    import re
    # The pattern we are looking for is "a followed by anything (*) ending in b".
    pattern = "ab*"
    # The search function will return a match object if the pattern is found.
    if re.search(pattern, txt):
        return True
    else:
        return False