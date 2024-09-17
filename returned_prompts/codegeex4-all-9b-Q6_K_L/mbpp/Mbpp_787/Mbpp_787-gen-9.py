import re
def text_match_three(text: str) -> bool:
    return bool(re.match(r"abbb", text))