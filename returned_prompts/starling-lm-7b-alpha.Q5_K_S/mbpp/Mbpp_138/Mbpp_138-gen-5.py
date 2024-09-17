
def is_Sum_Of_Powers_Of_Two(num:int):
    while num:
        if num % 2 == 0:
            return False
        num = num >> 1
    return True


