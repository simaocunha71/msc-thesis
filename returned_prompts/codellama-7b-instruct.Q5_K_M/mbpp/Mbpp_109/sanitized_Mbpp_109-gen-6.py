def odd_Equivalent(binary_str,n):
    binary_list = list(binary_str)
    for i in range(n):
        binary_list.append(binary_list[0])
        binary_list.pop(0)
    return binary_list.count('1')