def remove_whitespaces(s: str) -> str:
    return s.replace(" ", "")

assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'


