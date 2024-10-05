    count = 0
    for sentence in re.split(r'[.?!]', S):
        if sentence.startswith('I'):
            count += 1
    return count

