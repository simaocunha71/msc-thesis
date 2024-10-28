def digit_distance_nums(num1: int, num2: int) -> int:
    num1, num2 = str(num1), str(num2)
    if len(num1) > len(num2):
        num2 = '0' * (len(num1) - len(num2)) + num2
    elif len(num2) > len(num1):
        num1 = '0' * (len(num2) - len(num1)) + num1
    return sum(abs(int(num1[i]) - int(num2[i])) for i in range(len(num1)))