
def select_words(s, n):
    if not s:
        return []
    words = s.split()
    return [word for word in words if word.lower().count(word.lower()[0]) == n]

