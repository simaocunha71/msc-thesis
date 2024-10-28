def len_log(word_list):
    return len(max(word_list, key=len)) if word_list else 0