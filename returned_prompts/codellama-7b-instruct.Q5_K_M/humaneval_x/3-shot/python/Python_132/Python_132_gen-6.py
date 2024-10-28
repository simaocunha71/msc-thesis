    def is_nested(string):
        open_brackets = 0
        for c in string:
            if c == '[':
                open_brackets += 1
            elif c == ']':
                open_brackets -= 1
            if open_brackets < 0:
                return False
        return open_brackets == 0


