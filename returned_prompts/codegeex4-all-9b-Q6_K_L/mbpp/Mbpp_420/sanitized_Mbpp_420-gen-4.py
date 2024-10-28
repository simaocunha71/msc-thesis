def cube_Sum(n):
    even_nums = [i for i in range(2, 2*n+1, 2)]
    cube_sum = sum([x**3 for x in even_nums])
    return cube_sum