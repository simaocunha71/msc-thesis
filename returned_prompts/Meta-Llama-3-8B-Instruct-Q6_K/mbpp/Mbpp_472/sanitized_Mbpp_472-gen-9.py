def check_Consecutive(lst):
    return all(lst[i+1] - lst[i] == 1 for i in range(len(lst)-1)) and len(set(lst)) == len(lst) and lst[0] == min(lst) and lst[-1] == max(lst) and len(lst) > 1