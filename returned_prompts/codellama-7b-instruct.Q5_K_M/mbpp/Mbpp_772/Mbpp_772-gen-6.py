def remove_length(sentence, k):
    return " ".join([word for word in sentence.split() if len(word) != k])


