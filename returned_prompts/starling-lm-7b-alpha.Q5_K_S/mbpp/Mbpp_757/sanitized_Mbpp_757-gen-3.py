def count_reverse_pairs(string_list):
    count = 0
    for i in range(len(string_list)):
        for j in range(len(string_list)):
            if i != j:
                if string_list[i] == string_list[j][::-1]:
                    count += 1
    return count