
def correct_bracketing(brackets: str) -> bool:
    return len(brackets) % 2 == 0 and brackets.count("<") == brackets.count(">")
