def start_withp(words_list):
    result = []
    for words in words_list:
        for word in words.split():
            if word[0].lower() == 'p':
                result.append(word)
    return tuple(result[:2])