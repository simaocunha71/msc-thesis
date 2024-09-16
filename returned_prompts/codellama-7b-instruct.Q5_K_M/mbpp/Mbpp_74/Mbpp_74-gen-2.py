def is_samepatterns(patterns, strings):
    if len(patterns) != len(strings):
        return False
    for i in range(len(strings)):
        if patterns[i] != strings[i]:
            return False
    return True


