def validate(num):
    while num > 0:
        if num % 10 > (num % 10 <= num // 10):
            return False
        num = num // 10
    return True