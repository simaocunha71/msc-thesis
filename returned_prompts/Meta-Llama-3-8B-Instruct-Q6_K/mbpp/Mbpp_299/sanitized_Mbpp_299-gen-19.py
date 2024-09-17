def max_aggregate(tuples):
    aggregate = {}
    for student, score in tuples:
        if student in aggregate:
            aggregate[student] += score
        else:
            aggregate[student] = score
    return max(aggregate.items(), key=lambda x: x[1])