    boredoms = 0
    sentence = ""
    for word in S.split():
        if word in ['.', '?', '!']:
            if sentence.strip().lstrip().startswith('I'):
                boredoms += 1
            sentence = ""
        else:
            sentence += word + " "
    if sentence.strip().lstrip().startswith('I'):
        boredoms += 1
    return boredoms
