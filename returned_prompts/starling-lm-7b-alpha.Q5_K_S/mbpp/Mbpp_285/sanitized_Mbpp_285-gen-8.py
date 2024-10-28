def text_match_two_three(text):
    if 'a' in text and 'b' in text:
        if text.count('b') == 2 or text.count('b') == 3:
            return True
        else:
            return False
    else:
        return False