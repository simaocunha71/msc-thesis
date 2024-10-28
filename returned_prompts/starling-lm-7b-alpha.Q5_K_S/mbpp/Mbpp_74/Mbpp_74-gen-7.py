
def is_samepatterns(patterns:list, patterns2:list)->bool:
    if len(patterns) != len(patterns2):
        return False
    else:
        for i in range(len(patterns)):
            if patterns[i] != patterns2[i]:
                return False
        return True


