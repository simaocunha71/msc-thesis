    def is_happy(s: str) -> bool:
        if len(s) < 3:
            return False
        if len(s) == 3:
            return len(set(s)) == 3
        return len(set(s[:3])) == 3 and is_happy(s[1:])

    return is_happy(s)


