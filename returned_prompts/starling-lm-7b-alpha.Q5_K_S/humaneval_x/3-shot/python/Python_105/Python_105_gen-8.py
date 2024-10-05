    arr = [str(i) for i in arr if 1 <= i <= 9]
    arr.sort(reverse=True)
    result = []
    for i in arr:
        if i == '9':
            result.append("Nine")
        elif i == '8':
            result.append("Eight")
        elif i == '7':
            result.append("Seven")
        elif i == '6':
            result.append("Six")
        elif i == '5':
            result.append("Five")
        elif i == '4':
            result.append("Four")
        elif i == '3':
            result.append("Three")
        elif i == '2':
            result.append("Two")
        elif i == '1':
            result.append("One")
    return result



