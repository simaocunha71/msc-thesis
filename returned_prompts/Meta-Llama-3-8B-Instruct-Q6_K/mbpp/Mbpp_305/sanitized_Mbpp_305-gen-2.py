def start_withp(words):
    return tuple(word for word in words if word.startswith('p'))[:2]
    # return tuple(word for word in words if word.startswith('p') or word.startswith('P'))[:2]  # for case-insensitive search
    # return tuple(word for word in words if word[0].lower() == 'p')[:2]  # for case-insensitive search