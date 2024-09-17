def last_Digit_Factorial(num):
    if(num == 0):
        return 1
    else:
        last_Digit_Factorial = 1
        for i in range(1, num + 1):
            last_Digit_Factorial = (last_Digit_Factorial * i) % 10
        return last_Digit_Factorial