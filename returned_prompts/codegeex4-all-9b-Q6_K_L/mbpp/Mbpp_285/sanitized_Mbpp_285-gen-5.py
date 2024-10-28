def text_match_two_three(text: str) -> bool:
    # Check if the string contains 'a' followed by two or three 'b's
    if 'ab' in text and ('abb' in text or 'abbb' in text):
        return True
    else:
        return False