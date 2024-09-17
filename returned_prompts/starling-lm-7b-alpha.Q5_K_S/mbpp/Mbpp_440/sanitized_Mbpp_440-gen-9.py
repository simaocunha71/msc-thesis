def find_adverb_position(sentence):
    adverbs = ["quickly", "slowly", "clearly", "rapidly"]
    for i, word in enumerate(sentence.split()):
        if word in adverbs:
            return i, word
    return None, None