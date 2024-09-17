def extract_values(string: str) -> list:
    return [x.strip('"') for x in string.split(',')]


