def max_aggregate(tuples):
    aggregate_dict = {}
    for student, score in tuples:
        if student in aggregate_dict:
            aggregate_dict[student] += score
        else:
            aggregate_dict[student] = score
    return max(aggregate_dict.items(), key=lambda x: x[1])