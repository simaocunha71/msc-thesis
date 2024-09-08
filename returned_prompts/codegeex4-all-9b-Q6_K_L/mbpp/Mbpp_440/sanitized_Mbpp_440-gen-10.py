def find_adverb_position(sentence):
    adverb_positions = []
    for i, word in enumerate(sentence.split()):
        if word.endswith('ly'):
            adverb_positions.append((i, len(word), word))
    return adverb_positions[0] if adverb_positions else None