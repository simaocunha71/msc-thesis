    a_list=list(a)
    b_list=list(b)
    for i in range(len(b_list)):
        a_list.append(b_list[i])
        if ''.join(a_list) in a:
            return True
        a_list.pop()
    return False


