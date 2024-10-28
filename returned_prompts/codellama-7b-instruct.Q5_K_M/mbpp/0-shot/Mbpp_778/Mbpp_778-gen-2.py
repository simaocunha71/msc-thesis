def pack_consecutive_duplicates(my_list):
    return [[item, item] for item in my_list]


def pack_consecutive_duplicates(my_list):
    result = []
    for i in range(len(my_list)):
        if i == 0:
            current_item = my_list[i]
            current_item_list = [current_item]
        else:
            if my_list[i] == my_list[i - 1]:
                current_item_list.append(my_list[i])
            else:
                result.append(current_item_list)
                current_item = my_list[i]
                current_item_list = [current_item]
        if i == len(my_list) - 1:
            result.append(current_item_list)
    return result
