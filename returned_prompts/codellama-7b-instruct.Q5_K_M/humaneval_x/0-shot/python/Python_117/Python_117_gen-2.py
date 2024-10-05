
def select_words(s, n):
    words = []
    if s == "":
        return words
    for word in s.split():
        count = 0
        for letter in word:
            if letter.isalpha() and not letter.islower():
                count += 1
        if count == n:
            words.append(word)
    return words
