import re
def text_match_three(text):
    patterns = r'ab{3}'
    if re.search(patterns,  text):
        return True
    else:
        return False