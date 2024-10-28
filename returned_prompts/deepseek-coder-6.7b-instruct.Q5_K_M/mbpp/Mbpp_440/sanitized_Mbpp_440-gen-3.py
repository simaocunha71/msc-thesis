def find_adverb_position(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if words[i].endswith(','):
            words[i] = words[i][:-1]
    adverbs = ["very", "just", "so", "more", "most", "another", "hardly", "fairly", "rarely", "often",
               "usually", "often", "often", "often", "often"]
    for i in range(len(words)):
        if words[i] in adverbs:
            return i, i+1, words[i]
    return None