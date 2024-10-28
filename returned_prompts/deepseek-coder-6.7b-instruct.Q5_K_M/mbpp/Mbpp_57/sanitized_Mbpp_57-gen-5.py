def find_Max_Num(lst):
    lst = [str(i) for i in lst]
    lst.sort(reverse=True)
    return int(''.join(lst))