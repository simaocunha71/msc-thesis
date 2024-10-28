    result = []
    for elem in lst:
        count = 0
        for digit in elem:
            if int(digit) % 2 != 0:
                count += 1
        result.append(f"the number of odd elements {count}n the str{count}ng {count}f the {count}nput.")

    return result


