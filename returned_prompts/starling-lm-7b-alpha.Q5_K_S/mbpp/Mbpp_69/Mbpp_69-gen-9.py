
def is_sublist(list1, sub_list):
    if len(sub_list) > len(list1):
        return False
    else:
        for i in range(len(list1)):
            if len(sub_list) == 0:
                return True
            if list1[i] == sub_list[0]:
                if sub_list == list1[i:i+len(sub_list)]:
                    return True
    return False


