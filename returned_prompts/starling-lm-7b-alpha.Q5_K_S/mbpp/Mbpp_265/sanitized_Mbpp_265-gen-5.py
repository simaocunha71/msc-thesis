def list_split(input_list,n):
    temp_list = []
    for i in range(0,len(input_list),n):
        temp_list.append(input_list[i:i+n])
    return temp_list