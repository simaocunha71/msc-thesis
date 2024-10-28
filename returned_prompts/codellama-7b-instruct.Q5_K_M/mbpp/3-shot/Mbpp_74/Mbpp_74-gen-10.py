
def is_samepatterns(patterns: list, words: list) -> bool:
    for i in range(len(patterns)):
        if patterns[i] != words[i]:
            return False
    return True


