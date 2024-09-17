def max_aggregate(lst):
    aggregate = {}
    for student, score in lst:
        if student in aggregate:
            aggregate[student] += score
        else:
            aggregate[student] = score
    return max(aggregate.items(), key=lambda x: x[1])