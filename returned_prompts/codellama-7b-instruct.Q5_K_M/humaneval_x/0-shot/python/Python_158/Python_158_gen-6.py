
    unique_words = []
    for word in words:
        unique_words.append(len(set(word)))

    max_word = ""
    for i in range(len(words)):
        if unique_words[i] == max(unique_words):
            max_word = words[i]

    if max_word == "":
        max_word = words[unique_words.index(max(unique_words))]

    return max_word
