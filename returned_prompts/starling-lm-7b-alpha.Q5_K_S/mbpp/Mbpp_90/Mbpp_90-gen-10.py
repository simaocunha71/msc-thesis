
def len_log(words):
    longest_word = 0
    for word in words:
        if len(word) > longest_word:
            longest_word = len(word)
    return longest_word


