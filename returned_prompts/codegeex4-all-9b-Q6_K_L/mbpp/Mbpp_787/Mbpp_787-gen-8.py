import re
def text_match_three(text):
    pattern = re.compile(r"ab{3}")
    if pattern.match(text):
        return True
    else:
        return False

