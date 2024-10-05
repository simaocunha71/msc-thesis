    return sum(sentence.startswith("I") for sentence in re.split(r'[.?!]\s*', S))

