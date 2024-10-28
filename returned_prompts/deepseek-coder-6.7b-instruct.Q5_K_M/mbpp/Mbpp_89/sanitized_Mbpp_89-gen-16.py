def closest_num(n):
    str_n = str(n)
    for i in range(len(str_n)-1, -1, -1):
        if str_n[i] != '0':
            str_n_list = list(str_n)
            str_n_list[i] = str(int(str_n_list[i]) - 1)
            for j in range(i+1, len(str_n)):
                str_n_list[j] = '9'
            return int(''.join(str_n_list))
    return None