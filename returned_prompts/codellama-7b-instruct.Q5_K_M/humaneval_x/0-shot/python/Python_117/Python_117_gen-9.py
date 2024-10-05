
def select_words(s, n):
    if not s:
        return []

    words = s.split()
    consonants_count = [len(re.findall(r'[^aeiou]', word)) for word in words]
    return [word for word, count in zip(words, consonants_count) if count == n]
