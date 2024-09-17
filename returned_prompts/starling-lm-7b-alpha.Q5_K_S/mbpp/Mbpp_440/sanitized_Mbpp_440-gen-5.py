def find_adverb_position(sentence):
    adverb_list = ["quickly", "slowly", "clearly", "beautifully"]
    for i in range(len(sentence)):
        if sentence[i] in adverb_list:
            return i, sentence.find(sentence[i]), sentence[i]
    return -1