
def all_Characters_Same(word):
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            return False
    return True


