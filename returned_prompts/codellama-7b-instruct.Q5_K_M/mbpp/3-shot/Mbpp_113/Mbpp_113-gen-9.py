
def check_integer(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


