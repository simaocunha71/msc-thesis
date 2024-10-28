def replace_spaces(s: str) -> str:
    if " " in s:
        return s.replace(" ", "_")
    else:
        return s.replace("_", " ")