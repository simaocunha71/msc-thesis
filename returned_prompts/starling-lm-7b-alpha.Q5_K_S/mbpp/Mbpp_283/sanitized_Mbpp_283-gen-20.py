def validate(num):
    while num:
        if num%10 > (num//10)**len(str(num%10)):
            return False
        num = num//10
    return True