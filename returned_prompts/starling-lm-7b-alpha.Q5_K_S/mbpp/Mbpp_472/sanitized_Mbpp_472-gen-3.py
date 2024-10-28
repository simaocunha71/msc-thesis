def check_Consecutive(list):
    return all(list[i+1]-list[i] == 1 for i in range(len(list)-1))