def text_match_wordz_middle(text):
    return bool(re.search(r'[^\bz\b]', text))

print(text_text_match_wordz_middle("pythonzabc."))

B:
def text_match_wordz_middle(text):
    return any(char != 'z' for char in text[1:-1])

print(text_text_match_wordz_middle("pythonzabc."))

C:
def text_match_wordz_middle(text):
    return any(char == 'z' for char in text[1:-1])

print(text_text_match_wordz_middle("pythonzabc."))

D:
def text_match_wordz_middle(text):
    return bool(re.search(r'[z]{2,}', text))

print(text_text_match_wordz_middle("pythonzabc."))

E:
def text_match_wordz_middle(text):
    return bool(re.search(r'z[a-z]*z', text))

print(text_text_match_wordz_middle("pythonzabc."))

F:
def text_match_wordz_middle(text):
    return bool(re.search(r'[a-z]*z[a-z]*', text))

print(text_text_match_wordz_middle("pythonzabc."))

G:
def text_match_wordz_middle(text):
    return bool(re.search(r'[a-z]*z[a-z]*z[a-z]*', text))

print(text_text_match_wordz_middle("pythonzabc."))

H:
def text_match_wordz_middle(text):
    return bool(re.search(r'[a-z]*z[a-z]*z[a-z]*z[a-z]*', text))

print(text_text_match_wordz_middle("pythonzabc."))

I:
def text_match_wordz_middle(text