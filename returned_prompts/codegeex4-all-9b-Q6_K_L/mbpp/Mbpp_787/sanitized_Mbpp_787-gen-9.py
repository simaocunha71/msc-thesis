import re
def text_match_three(text):
    pattern = re.compile(r'a.*b.*b.*b')
    if pattern.match(text):
        return True
    else:
        return False