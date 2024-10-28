    unique = []
    for number in x:
        for digit in str(number):
            if int(digit) % 2 != 0:
                unique.append(number)
                break

    return sorted(list(set(unique)))


