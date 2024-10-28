def first_Digit(n):
    if n>=0:
        while n>=10:
            n = n//10
        return n
    else:
        return "Invalid Input"