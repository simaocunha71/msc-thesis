def check_occurences(tuples):
    occurrences = {}
    for t in tuples:
        if t in occurrences:
            occurrences[t] += 1
        else:
            occurrences[t] = 1
    return occurrences