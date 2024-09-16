def toggle_string(s):
    def upcase(c):
        if c.islower():
            return c.upper()
        else:
            return c.lower()
    return ''.join(map(upcase, s))