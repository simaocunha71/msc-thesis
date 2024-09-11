def list_split(input_list,n):
    temp_list = []
    for i in range(0,len(input_list),n):
        temp_list.append(input_list[i:i+n])
    return temp_list

list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

# def list_split(input_list,n):
#     temp_list = []
#     for i in range(0,len(input_list),n):
#         temp_list.append(input_list[i:i+n])
#     return temp_list

# list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


# def list_split(input_list,n):
#     temp_list = []
#     for i in range(0,len(input_list),n):
#         temp_list.append(input_list[i:i+n])
#     return temp_list

# list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


# def list_split(input_list,n):
#     temp_list = []
#     for i in range(0,len(input