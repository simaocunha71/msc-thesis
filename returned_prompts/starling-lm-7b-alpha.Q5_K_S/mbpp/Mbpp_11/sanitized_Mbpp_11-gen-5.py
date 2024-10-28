def remove_Occ(string,character):
    string_list = list(string)
    for i in range(len(string_list)):
        if string_list[i] == character:
            if i == 0:
                string_list.pop(i)
                break
            else:
                string_list.pop(i)
                break

    for i in range(len(string_list)-1,-1,-1):
        if string_list[i] == character:
            if i == len(string_list)-1:
                string_list.pop(i)
                break
            else:
                string_list.pop(i)
                break
    return ''.join(string_list)