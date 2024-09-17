def issort_list(input_list):
    for x in range(len(input_list)-1):
        if input_list[x+1] < input_list[x]:
            return False
    return True