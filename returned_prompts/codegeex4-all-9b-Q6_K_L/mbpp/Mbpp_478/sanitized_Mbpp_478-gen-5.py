def remove_lowercase(s: str) -> str:
    # Find the first uppercase character
    upper_index = next((i for i, c in enumerate(s) if c.isupper()), len(s))
    return s[:upper_index]