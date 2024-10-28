
def reverse_delete(s,c):
    s_list = list(s)
    for i in s_list:
        if i in c:
            s_list.remove(i)
    return ''.join(s_list), ''.join(s_list) == s_list[::-1]


