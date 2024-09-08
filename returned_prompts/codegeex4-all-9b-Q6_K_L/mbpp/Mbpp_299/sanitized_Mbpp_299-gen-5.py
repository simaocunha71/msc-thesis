def max_aggregate(data):
    aggregate_data = {}
    for name, score in data:
        if name in aggregate_data:
            aggregate_data[name] += score
        else:
            aggregate_data[name] = score
    max_name, max_score = max(aggregate_data.items(), key=lambda x: x[1])
    return (max_name, max_score)