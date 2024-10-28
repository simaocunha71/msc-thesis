def is_sublist(li,sub_li):
    if len(sub_li) > len(li):
        return False
    for i in range(len(li)-len(sub_li)+1):
        if li[i:i+len(sub_li)] == sub_li:
            return True
    return False