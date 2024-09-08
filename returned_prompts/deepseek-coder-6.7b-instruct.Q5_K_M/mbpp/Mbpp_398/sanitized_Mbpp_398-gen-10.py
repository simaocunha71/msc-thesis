def sum_of_digits(lst):
    res = []
    for num in lst:
        temp = 0
        for digit in str(num):
            temp += int(digit)
        res.append(temp)
    return res