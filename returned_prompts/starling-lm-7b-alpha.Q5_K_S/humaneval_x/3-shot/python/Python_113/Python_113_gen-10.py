    result = []
    for i in range(len(lst)):
        count = 0
        for j in lst[i]:
            if int(j) % 2 != 0:
                count += 1
        result.append("the number of odd elements " + str(count) + "n the str" + str(count) + "ng " + str(count) + "f the " + str(count) + "nput.")
    return result


