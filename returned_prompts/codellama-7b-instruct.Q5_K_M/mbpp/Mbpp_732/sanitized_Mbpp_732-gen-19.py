def replace_specialchar(str1: str) -> str:
    str1 = str1.replace(' ', ':').replace(',', ':').replace('.', ':')
    return str1