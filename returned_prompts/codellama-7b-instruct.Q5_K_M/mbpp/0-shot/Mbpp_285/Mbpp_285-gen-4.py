def text_match_two_three(text):
    if 'a' in text:
        if text.count('a') > 1:
            if text.count('b') == text.count('a') - 1:
                return True
    return False

