def find_Index(n):
    triangular_numbers = [i*(i+1)//2 for i in range(1, 10000)]
    for i in range(len(triangular_numbers)):
        if len(str(triangular_numbers[i])) == n:
            return i + 1
    return None