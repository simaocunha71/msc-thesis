    result = 0
    for sentence in re.findall(r'[^.!?]*[.!?]', S):
        if sentence.startswith('I'):
            result += 1

    return result

