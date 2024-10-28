def max_aggregate(tuples):
    max_score, name = 0, ''
    for tup in tuples:
        name, score = tup
        if score > max_score:
            max_score = score
            name = name
    return (name, max_score)