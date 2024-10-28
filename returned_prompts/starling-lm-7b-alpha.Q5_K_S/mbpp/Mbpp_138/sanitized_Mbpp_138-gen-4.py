def is_Sum_Of_Powers_Of_Two(n):
    return (n > 0) and (bin(n).count('1') == 1)