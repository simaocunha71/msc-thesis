def move_num(s):
    digits = [char for char in s if char.isdigit()]
    letters = [char for char in s if not char.isdigit()]
    return "".join(letters + digits)