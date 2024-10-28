def find_adverb_position(sentence):
    adverb_positions = []
    words = sentence.split()
    for i, word in enumerate(words):
        if word.endswith('ly'):
            adverb_positions.append((i, len(sentence.split()[i]), word))
    return adverb_positions[0] if adverb_positions else None