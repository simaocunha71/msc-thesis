def text_match_wordz(text):
    words = text.split()
    for word in words:
        if 'z' in word:
            return True
    return False

