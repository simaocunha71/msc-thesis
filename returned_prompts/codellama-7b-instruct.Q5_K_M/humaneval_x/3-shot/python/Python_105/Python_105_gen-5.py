    names = { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine' }
    res = []
    for num in arr:
        if 1 <= num <= 9:
            res.append(names[num])
        elif num > 9:
            res.append(str(num))
    return res


