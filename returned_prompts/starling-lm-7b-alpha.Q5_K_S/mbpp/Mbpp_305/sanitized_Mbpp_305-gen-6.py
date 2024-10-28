def start_withp(words_list):
    result = []
    for word in words_list:
        if word.startswith('p'):
            result.append(word)
    return result