def find_adverb_position(sentence):
    for i in range(len(sentence)):
        if sentence[i] in ['very', 'also', 'somewhat', 'still', 'just', 'clearly', 'mostly', 'already', 'finally']:
            return i, i+len(sentence[i]), sentence[i]
    return -1
