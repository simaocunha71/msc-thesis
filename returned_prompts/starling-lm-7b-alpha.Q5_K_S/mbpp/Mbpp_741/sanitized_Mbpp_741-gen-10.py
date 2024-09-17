def all_Characters_Same(word):
    if len(word) == 1:
        return True
    if len(word) > 1:
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                return False
        return True