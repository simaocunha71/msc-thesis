def toggle_string(string):
    res = []
    for c in string:
        if c.isupper():
            res.append(c.lower())
        else:
            res.append(c.upper())
    return "".join(res)