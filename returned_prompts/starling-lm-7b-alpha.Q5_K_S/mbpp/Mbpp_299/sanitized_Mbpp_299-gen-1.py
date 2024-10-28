def max_aggregate(l):
    result = []
    for i in l:
        if i[0] in result:
            if i[1] > result[result.index(i[0])][1]:
                result.remove(i[0])
                result.append(i)
        else:
            result.append(i)
    return (max(result),sum(i[1] for i in l))