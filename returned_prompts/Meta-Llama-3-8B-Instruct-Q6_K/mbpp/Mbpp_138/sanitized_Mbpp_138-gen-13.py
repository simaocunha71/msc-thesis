def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    powers = [2 ** i for i in range(1, n.bit_length() + 1)]
    for i in range(len(powers)):
        for j in range(i, len(powers)):
            if sum(powers[i:j+1]) == n:
                return True
    return False