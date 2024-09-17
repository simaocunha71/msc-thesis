def find_Index(n):
    i = 1
    while True:
        triangular_num = i*(i+1)//2
        if len(str(triangular_number)) == n:
            return i
        i += 1