    # split the string by '.', '?' or '!' to get a list of sentences
    sentences = S.split('[.!?]')
    boredom_count = 0
    for sentence in sentences:
        sentence = sentence.strip()  # remove leading/trailing spaces
        if sentence and sentence[0].lower() == 'i':  # check if sentence starts with 'I'
            boredom_count += 1
    return boredom_count
