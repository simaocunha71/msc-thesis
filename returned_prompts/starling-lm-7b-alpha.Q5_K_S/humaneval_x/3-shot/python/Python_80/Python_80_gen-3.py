    def is_happy(s):
        if len(s) < 3:
            return False
        char_set = set()
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2]:
                return False
            char_set.add(s[i:i + 3])
        return len(char_set) == len(s) - 2


