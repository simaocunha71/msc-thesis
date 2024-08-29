def find_adverb_position(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        if words[i].lower() in ['well', 'not', 'just', 'so', 'only', 'too']:
            return i, i+1, words[i]
    return None