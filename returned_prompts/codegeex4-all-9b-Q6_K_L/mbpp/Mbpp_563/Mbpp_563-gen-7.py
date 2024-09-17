def extract_values(s: str) -> list:
    return [i.strip('"') for i in s.split(",")]


