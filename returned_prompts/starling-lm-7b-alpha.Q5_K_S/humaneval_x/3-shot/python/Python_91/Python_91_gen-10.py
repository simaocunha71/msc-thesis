    result = 0
    last_sentence = ""
    for word in S.split():
        if word == "I":
            result += 1

    return result


