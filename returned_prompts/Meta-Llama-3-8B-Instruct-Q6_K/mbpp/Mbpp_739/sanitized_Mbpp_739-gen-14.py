def find_Index(n):
    i = 1
    triangular_nums = []
    while True:
        triangular_num = sum(range(1, i+1))
        triangular_nums.append(triangular_num)
        if str(triangular_num).__len__() == n:
            return triangular_nums.index(triangular_num)
        i += 1