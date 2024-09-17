def remove_uppercase(s: str) -> str:
    return ''.join(filter(lambda x: not x.isupper(), s))