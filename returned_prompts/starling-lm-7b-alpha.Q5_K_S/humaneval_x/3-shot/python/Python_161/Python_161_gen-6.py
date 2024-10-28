    def f(c):
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ord(c) - ord("A")] if c.isupper() else "abcdefghijklmnopqrstuvwxyz"[ord(c) - ord("a")]

    return "".join(map(f, s)) if any(c.isalpha() for c in s) else s[::-1]


