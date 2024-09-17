def count_reverse_pairs(string_list: list) -> int:
    count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if string_list[i][::-1] == string_list[j]:
                count += 1
    return count