    result = []

    for element in lst:
        count = 0

        for char in element:
            if int(char) % 2 != 0:
                count += 1

        result.append(f"the number of odd elements {count}n the str{count}ng {count} of the {count}nput.")

    return result


