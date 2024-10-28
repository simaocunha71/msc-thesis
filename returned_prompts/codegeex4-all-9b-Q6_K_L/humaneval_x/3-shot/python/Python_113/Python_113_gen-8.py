    result = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 != 0:
                count += 1
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(count, count, count, count))
    return result

