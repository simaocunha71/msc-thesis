    result = []
    for s in lst:
        odd_count = 0
        for c in s:
            if int(c) % 2 == 1:
                odd_count += 1
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(odd_count, odd_count, s, odd_count))
    return result


