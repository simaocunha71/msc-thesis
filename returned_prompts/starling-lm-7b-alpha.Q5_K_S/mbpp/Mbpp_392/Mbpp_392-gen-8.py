
def get_max_sum(n):
    if n == 0 or n == 1:
        return 0
    if n == 2 or n == 3 or n == 4 or n == 5:
        return n
    f_n_2 = get_max_sum(n//2)
    f_n_3 = get_max_sum(n//3)
    f_n_4 = get_max_sum(n//4)
    f_n_5 = get_max_sum(n//5)
    return max(f_n_2 + f_n_3 + f_n_4 + f_n_5,n)


