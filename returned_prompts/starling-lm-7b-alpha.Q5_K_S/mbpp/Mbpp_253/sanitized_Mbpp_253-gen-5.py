def count_integer(input_list):
    count=0
    for i in input_list:
        if isinstance(i, int):
            count+=1
    return count