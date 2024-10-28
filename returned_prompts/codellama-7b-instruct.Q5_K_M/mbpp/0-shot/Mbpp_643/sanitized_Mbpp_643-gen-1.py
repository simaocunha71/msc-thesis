def text_match_wordz_middle(text):
    if text.startswith("z") and text.endswith("z"):
        return any("z" in w for w in text.split())
    return False