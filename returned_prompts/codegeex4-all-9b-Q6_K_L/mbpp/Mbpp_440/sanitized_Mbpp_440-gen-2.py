def find_adverb_position(sentence):
    adverb = ""
    position = -1
    for i in range(len(sentence)):
        if sentence[i].isalpha() and sentence[i-1] == " ":
            adverb = sentence[i]
            position = i
            break
    return position, position+len(adverb), adverb