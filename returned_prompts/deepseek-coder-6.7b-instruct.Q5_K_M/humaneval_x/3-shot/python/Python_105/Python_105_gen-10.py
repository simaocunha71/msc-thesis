    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = []

    for i in sorted(arr):
        if 1 <= i <= 9:
            result.append(names[i-1])

    return result[::-1]


