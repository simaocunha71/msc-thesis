
def is_Sum_Of_Powers_Of_Two(n):
    if n == 1:
        return True
    if n == 0:
        return False
    while(n % 2 == 0):
        n = n >> 1
    return is_Sum_Of_Powers_Of_Two(n - 1)


