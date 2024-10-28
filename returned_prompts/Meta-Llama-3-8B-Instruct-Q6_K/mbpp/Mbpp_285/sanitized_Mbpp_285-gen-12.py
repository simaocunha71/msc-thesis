def text_match_two_three(text):
    if 'a' in text and 'b' in text:
        b_count = text.count('b')
        if b_count >= 2 and b_count <= 3:
            return True
    return False