    def is_happy(s: str) -> bool:
        if len(s) < 3:
            return False
        return len(set(s[i:i+3] for i in range(len(s)) if i+2 < len(s))) == len(s) - 2


