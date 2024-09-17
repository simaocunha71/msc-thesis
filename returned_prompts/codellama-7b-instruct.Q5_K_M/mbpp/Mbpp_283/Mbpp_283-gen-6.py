
def validate(num):
    digits = [int(i) for i in str(num)]
    for i in range(1,10):
        if digits.count(i) > i:
            return False
    return True


