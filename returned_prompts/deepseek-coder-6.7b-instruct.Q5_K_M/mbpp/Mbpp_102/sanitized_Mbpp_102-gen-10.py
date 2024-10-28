def snake_to_camel(s: str) -> str:
    return ''.join(word.capitalize() for word in s.split('_'))