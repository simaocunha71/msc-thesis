def find_adverb_position(sentence):
    adverbs = ["clearly", "easily", "often", "always", "never", "still", "just", "again", "further", "even", "night"]
    words = sentence.split()
    for i in range(len(words)):
        if words[i] in adverbs:
            return i, i+1, words[i]
    return None