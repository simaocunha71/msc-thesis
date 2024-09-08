def find_adverb_position(sentence):
    words = sentence.split()
    for i, word in enumerate(words):
        if word.endswith('ly'):
            return (i, sum(len(w) for w in words[:i+1]), word)
    return None