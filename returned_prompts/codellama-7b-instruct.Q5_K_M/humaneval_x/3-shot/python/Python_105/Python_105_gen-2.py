    arr = sorted(arr)
    arr = arr[::-1]
    arr = [str(x) for x in arr]
    arr = [int(x) for x in arr]
    arr = [str(x) for x in arr]
    arr = [x.lower() for x in arr]
    arr = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

    for i in range(len(arr)):
        arr[i] = arr[i] if (arr[i] in str(arr)) else ''

    return arr


