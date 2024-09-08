def replace_spaces(s):
    if " " in s:
        return s.replace(" ", "_")
    else:
        return s.replace("_", " ")