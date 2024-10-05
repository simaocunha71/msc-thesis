
    unique_list = []
    for number in l:
        if number not in unique_list:
            unique_list.append(number)
    return sorted(unique_list)


print(unique_v4([5, 3,