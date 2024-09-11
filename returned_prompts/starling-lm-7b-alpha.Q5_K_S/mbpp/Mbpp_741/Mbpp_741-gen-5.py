"""
def all_Characters_Same(word):
    if len(word) == 1:
        return True
    else:
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                return False
    return True

assert all_Characters_Same("python") == False
"""

