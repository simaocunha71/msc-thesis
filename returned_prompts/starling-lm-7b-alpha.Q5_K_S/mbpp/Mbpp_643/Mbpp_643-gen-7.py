"""
def text_match_wordz_middle(text):
    if len(text) < 3:
        return False
    if text[0] == 'z' or text[len(text)-1] == 'z':
        return False
    for i in range(1,len(text)-1):
        if text[i] == 'z':
            return True
    return False
"""
def text_match_wordz_middle(text):
    if len(text) < 3:
        return False
    if text[0] == 'z' or text[len(text)-1] == 'z':
        return False
    for i in range(1,len(text)-1):
        if text[i] == 'z':
            return True
    return False


# Assert
assert text_match_wordz_middle("pythonzabc.") == True
assert text_match_wordz_middle("pythonabc.") == False
assert text_match_wordz_middle("pythonzabc") == False
assert text_match_wordz_middle("pythonz") == False
assert text_match_wordz_middle("pythonz.") == True
assert text_match_wordz_middle(".") == False
assert text_match_wordz_middle("z.") == False

print("All assertions passed")

































```