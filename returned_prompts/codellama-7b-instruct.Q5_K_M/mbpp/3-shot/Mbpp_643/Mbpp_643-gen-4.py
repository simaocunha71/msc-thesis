
def text_match_wordz_middle(text: str) -> bool:
    if text.startswith("z") and text.endswith("z"):
        if "z" in text[1:-1]:
            return True
        else:
            return False
    else:
        return False


