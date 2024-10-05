    result = []
    for i in range(len(lst)):
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(
            lst[i].count(str(x)) for x in range(10) if (int(x) & 1) == 1,
            i+1, lst[i], i+1))
    return result


