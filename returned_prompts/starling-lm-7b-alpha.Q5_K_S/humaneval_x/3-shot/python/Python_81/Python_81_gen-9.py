    result = []
    for g in grades:
        if g >= 4.0:
            result.append('A+')
        elif g >= 3.7:
            result.append('A')
        elif g >= 3.3:
            result.append('A-')
        elif g >= 3.0:
            result.append('B+')
        elif g >= 2.7:
            result.append('B')
        elif g >= 2.3:
            result.append('B-')
        elif g >= 2.0:
            result.append('C+')
        elif g >= 1.7:
            result.append('C')
        elif g >= 1.3:
            result.append('C-')
        elif g >= 1.0:
            result.append('D+')
        elif g >= 0.7:
            result.append('D')
        elif g >= 0.0:
            result.append('D-')
        elif g >= -0.0:
            result.append('E')
    return result


