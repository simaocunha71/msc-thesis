def find_adverb_position(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        if words[i].lower() in ['very', 'just', 'so', 'much', 'too', 'as', 'as much', 'as often', 'as often as', 'often', 'often as', 'as much as', 'very much', 'very often', 'very often as']:
            return i, i+1, words[i]
    return -1, -1, ""