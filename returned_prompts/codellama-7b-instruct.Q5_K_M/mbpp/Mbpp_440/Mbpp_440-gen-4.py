def find_adverb_position(sentence):
    for i in range(len(sentence)):
        if sentence[i] in ["very", "also", "well", "quite", "simply", "clearly", "frankly", "basically", "actually"]:
            return (i, i+len(sentence[i]), sentence[i])

    return (None, None, None)
