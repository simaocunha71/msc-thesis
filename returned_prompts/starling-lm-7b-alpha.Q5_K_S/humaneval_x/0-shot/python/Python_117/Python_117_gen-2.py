
def select_words(s, n):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    words = []
    curr_word = ""
    for c in s:
        if c in consonants:
            curr_word += c
            if len(curr_word) == n:
                words.append(curr_word)
                curr_word = ""
        elif c == ' ':
            if len(curr_word) == n:
                words.append(curr_word)
                curr_word = ""
        else:
            curr_word = ""
    if curr_word:
        words.append(curr_word)
    return words


# Test
print(select_words("Mary had a little lamb", 4) == ["little"])
print(select_words("Mary had a little lamb", 3) == ["Mary", "lamb"])
print(select_words("simple white space", 2) == [])
print(select_words("Hello world", 4) == ["world"])
print(select_words("Uncle sam", 3) == ["Uncle"])



























































































































































































































