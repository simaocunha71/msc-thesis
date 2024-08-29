def remove_whitespaces(s: str) -> str:
    return s.replace(' ', '')

print(remove_whitespaces(' Google    Flutter '))  # should return 'GoogleFlutter'

