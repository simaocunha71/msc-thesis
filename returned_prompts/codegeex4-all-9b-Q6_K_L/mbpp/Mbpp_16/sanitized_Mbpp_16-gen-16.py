def text_lowercase_underscore(s):
    import re
    if re.match("^[a-z]+(_[a-z]+)*$", s):
        return True
    else:
        return False