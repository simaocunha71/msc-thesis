def len_log(words):
    max_len = max(len(word) for word in words)
    return max_len

assert len_log(["python","PHP","bigdata"]) == 7

