def count_reverse_pairs(str_list: list) -> int:
    count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if str_list[i] == str_list[j][::-1]:
                count += 1
    return count