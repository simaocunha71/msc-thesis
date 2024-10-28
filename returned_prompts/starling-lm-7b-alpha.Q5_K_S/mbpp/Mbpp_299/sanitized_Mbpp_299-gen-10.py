def max_aggregate(tuples_list):
    """Calculate the maximum aggregate from the list of tuples."""
    result = []
    for i in range(len(tuples_list)):
        if result == []:
            result.append(tuples_list[i])
        else:
            if result[0][1] < tuples_list[i][1]:
                result = [tuples_list[i]]
            elif result[0][1] == tuples_list[i][1]:
                result.append(tuples_list[i])
    return result