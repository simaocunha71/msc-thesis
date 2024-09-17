
def dif_Square(num: int):
    for i in range(1,num):
        if i*i - (num-i) == num:
            return True
    return False


