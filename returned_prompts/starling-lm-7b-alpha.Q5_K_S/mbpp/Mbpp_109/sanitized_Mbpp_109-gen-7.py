def odd_Equivalent(s, n):
    s_list = list(s)
    count = 0
    for i in range(len(s_list)):
        for j in range(n):
            s_list[i] = s_list[i] if s_list[i] == '0' else '1'
        if s_list[i] == '1':
            count += 1
    return count