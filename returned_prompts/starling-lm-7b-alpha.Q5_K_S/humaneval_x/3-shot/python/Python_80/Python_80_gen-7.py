    def is_happy(s: str) -> bool:
        if len(s) < 3:
            return False

        return len(set(s[i:i+3] for i in range(0, len(s)-2, 3))) == len(s[0:3:3])


