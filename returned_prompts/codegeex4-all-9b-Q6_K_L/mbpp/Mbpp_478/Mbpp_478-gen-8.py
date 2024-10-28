def remove_lowercase(s: str) -> str:
    return "".join([char for char in s if not char.islower()])