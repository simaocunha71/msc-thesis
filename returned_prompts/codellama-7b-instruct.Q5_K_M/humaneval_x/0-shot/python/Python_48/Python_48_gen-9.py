
def is_palindrome(text: str):
    return text.lower().replace(' ', '') == text.lower().replace(' ', '').replace('-', '').replace('.', '').replace(',', '')[::-1]
