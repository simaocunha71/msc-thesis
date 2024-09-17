
def text_match_three(text: str) -> bool:
    if len(text) < 4:
        return False
    elif len(text) == 4 and text[0] == "a" and text[1:] == "bbb":
        return True
    else:
        return False


