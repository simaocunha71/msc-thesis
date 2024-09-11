def max_aggregate(lst):
    total_dict = {}
    for name, score in lst:
        if name in total_dict:
            total_dict[name] += score
        else:
            total_dict[name] = score
    return max(total_dict.items(), key=lambda x: x[1])  # return the tuple with the maximum total score