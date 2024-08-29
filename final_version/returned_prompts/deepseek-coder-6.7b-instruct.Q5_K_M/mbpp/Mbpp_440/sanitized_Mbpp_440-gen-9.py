def find_adverb_position(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        if words[i].endswith(','):
            words[i] = words[i][:-1]
        if words[i] in ['very', 'just', 'so', 'only', 'too']:
            return i, i+1, words[i]
    return None