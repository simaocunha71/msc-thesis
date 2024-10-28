
def toggle_string(s: str) -> str:
    new_str = ""
    for i in s:
        if i.isupper():
            new_str += i.lower()
        else:
            new_str += i.upper()
    return new_str


