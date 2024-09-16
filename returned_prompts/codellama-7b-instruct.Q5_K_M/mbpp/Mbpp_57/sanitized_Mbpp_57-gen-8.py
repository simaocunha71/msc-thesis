def find_Max_Num(my_list):
    return int(''.join(sorted(map(str, my_list), reverse=True)))