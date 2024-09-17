def armstrong_number(num: int):
    digits = [int(i) for i in str(num)]
    return sum([i ** len(digits) for i in digits]) == num