def max_aggregate(tuples):
    max_name = ""
    max_score = 0
    for t in tuples:
        if t[1] > max_score:
            max_name = t[0]
            max_score = t[1]
    return (max_name, max_score)