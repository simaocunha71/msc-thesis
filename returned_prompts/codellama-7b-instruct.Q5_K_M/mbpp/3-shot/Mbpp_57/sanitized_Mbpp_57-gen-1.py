def find_Max_Num(digits):
    digits.sort(reverse=True)
    num = ''
    for i in digits:
        num += str(i)
    return int(num)