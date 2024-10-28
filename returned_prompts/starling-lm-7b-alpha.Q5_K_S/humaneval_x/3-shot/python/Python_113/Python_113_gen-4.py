    result = []
    for s in lst:
        odds = 0
        for c in s:
            if int(c) % 2 == 1:
                odds += 1
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(odds, odds, s, odds))
    return result


