    result = []
    for string in lst:
        count = sum(1 for char in string if int(char) % 2 != 0)
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(count,count,count,count))
    return result


