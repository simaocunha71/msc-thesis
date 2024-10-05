    words = s.split(" ")
    word_list = []
    for word in words:
        word_list.append("".join(sorted(word)))
    return " ".join(word_list)


