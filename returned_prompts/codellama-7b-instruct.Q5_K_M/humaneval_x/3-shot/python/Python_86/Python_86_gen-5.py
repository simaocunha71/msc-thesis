    words = s.split(" ")
    shuffled_words = []
    for word in words:
        word_list = list(word)
        word_list.sort()
        shuffled_words.append("".join(word_list))
    return " ".join(shuffled_words)


