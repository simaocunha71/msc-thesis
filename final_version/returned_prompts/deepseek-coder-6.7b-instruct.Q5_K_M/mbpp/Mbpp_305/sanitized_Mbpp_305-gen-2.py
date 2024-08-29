def start_withp(words):
    result = []
    for word in words:
        split_word = word.split()
        for sw in split_word:
            if sw.lower().startswith('p'):
                result.append(sw)
    return tuple(result)