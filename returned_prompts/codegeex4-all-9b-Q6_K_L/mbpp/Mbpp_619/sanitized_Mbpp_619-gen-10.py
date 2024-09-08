def move_num(s: str) -> str:
    # Filter out numbers and concatenate the rest
    letters = ''.join([i for i in s if not i.isdigit()])
    # Filter out letters and concatenate the rest
    numbers = ''.join([i for i in s if i.isdigit()])
    # Concatenate the letters and numbers
    return letters + numbers