def replace_spaces(s):
    s = s.replace(" ", "_")
    s = s.replace("_", " ")
    return s.replace(" ", "_")  # This step is to replace the remaining spaces with underscores