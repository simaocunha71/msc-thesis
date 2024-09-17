def is_Sum_Of_Powers_Of_Two(n:int)->bool:
    while n:
        if n & 1:
            return False
        n >>= 1
    return True