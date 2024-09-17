def find_adverb_position(sentence):
    # Create a list of adverbs
    adverbs = ["quickly", "slowly", "clearly", "quickly", "slowly"]
    # Split the sentence into words
    words = sentence.split()
    # Find the position of the first adverb
    for i, word in enumerate(words):
        if word in adverbs:
            # Return the position of the first adverb
            return i, words.index(word), word