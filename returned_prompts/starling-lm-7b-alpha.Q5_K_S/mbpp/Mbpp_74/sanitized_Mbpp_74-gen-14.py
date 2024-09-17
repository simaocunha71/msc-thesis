def is_samepatterns(str_pattern, char_pattern):
    if len(str_pattern) != len(char_pattern):
        return False
    else:
        for i in range(len(str_pattern)):
            if str_pattern[i] != char_pattern[i]:
                return False
        return True